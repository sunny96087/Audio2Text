import torch
import whisper
import os
import ssl
from pathlib import Path
from tqdm import tqdm
from typing import Literal

# 使用者設定區域 👩🏻‍💻 ======================
# (可自訂) 選擇模型大小：tiny, base, small, medium, large, large-v2, large-v3
MODEL_SIZE = "medium"

# (可自訂) 選擇語言模式 🌏 
# 'zh': 中文
# 'zh-en': 中英混合
# 'en': 英文
# 'ja': 日文
LANGUAGE_MODE = "zh-en"

# 設定運行裝置 💻 
DEVICE = "cpu"  # 目前強制使用 CPU，避免 MPS 相容性問題

# 語言提示設定 📝 
LANGUAGE_PROMPTS = {
    "zh": {
        "language": "zh",
        "prompt": "請轉錄以下繁體中文的內容："
    },
    "zh-en": {
        "language": "zh",
        "prompt": "請轉錄以下內容，可能包含中文和英文："
    },
    "en": {
        "language": "en",
        "prompt": "Please transcribe the following English content:"
    },
    "ja": {
        "language": "ja",
        "prompt": "以下の日本語の内容を文字起こししてください："
    }
}
# ===========================================

def get_unique_filename(base_path: str) -> str:
    """
    如果檔案存在，自動在檔名後加上編號
    例如：test.txt -> test(1).txt -> test(2).txt
    """
    if not os.path.exists(base_path):
        return base_path
    
    directory = os.path.dirname(base_path)
    filename = os.path.basename(base_path)
    name, ext = os.path.splitext(filename)
    
    counter = 1
    while os.path.exists(base_path):
        base_path = os.path.join(directory, f"{name}({counter}){ext}")
        counter += 1
    
    return base_path

def transcribe_audio_files():
    # 設定 SSL 上下文
    ssl._create_default_https_context = ssl._create_unverified_context

    # 取得語言設定
    lang_config = LANGUAGE_PROMPTS.get(LANGUAGE_MODE, LANGUAGE_PROMPTS["zh"])
    
    print(f"使用模型: {MODEL_SIZE}")
    print(f"語言模式: {LANGUAGE_MODE}")
    print(f"語言提示: {lang_config['prompt']}")
    
    # 設定快取目錄
    cache_dir = Path("./whisper_cache")
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ["XDG_CACHE_HOME"] = str(cache_dir)

    # 設定輸入和輸出資料夾
    input_folder = "audio_files"    # 音訊檔案資料夾
    output_folder = "transcripts"   # 輸出文字檔案資料夾
    
    # 確保輸出資料夾存在
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # 載入模型（只需載入一次）
    print("載入 Whisper 模型中...")
    model = whisper.load_model(MODEL_SIZE, device=DEVICE)
    
    # 支援的音訊格式
    audio_extensions = ('.mp3', '.wav', '.m4a', '.flac', '.mov', '.mp4', '.m4v')
    
    # 取得輸入資料夾中所有音訊檔案
    audio_files = [f for f in os.listdir(input_folder) 
                  if f.lower().endswith(audio_extensions)]
    
    if not audio_files:
        print(f"在 {input_folder} 資料夾中沒有找到音訊檔案")
        return
    
    # 處理每個音訊檔案
    for audio_file in audio_files:
        print(f"\n開始處理: {audio_file}")
        input_path = os.path.join(input_folder, audio_file)
        
        try:
            print("正在轉錄音訊...")
            # 處理音頻檔案，指定繁體中文
            result = model.transcribe(
                                    input_path,
                                    prompt=lang_config["prompt"],
                                    language=lang_config["language"],
                                    verbose=True)
            
            # 獲取不帶副檔名的檔案名稱
            file_name = os.path.splitext(audio_file)[0]
            output_path = os.path.join(output_folder, f"{file_name}.txt")

            # 確保檔名不重複
            output_path = get_unique_filename(output_path)
            
            # 將結果保存為txt檔案
            with open(output_path, "w", encoding='utf-8') as file:
                file.write(result["text"])
            
            print(f"✓ 轉錄完成：{output_path}")
            
        except Exception as e:
            print(f"處理 {audio_file} 時發生錯誤: {str(e)}")

if __name__ == "__main__":
    transcribe_audio_files()