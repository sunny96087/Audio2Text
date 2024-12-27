# 音訊轉文字工具 🎙️➡️📝

這是一個簡單好用的音訊轉文字工具！它可以幫您把各種音訊檔案（像是錄音、影片的聲音等）自動轉換成文字。使用的是 OpenAI 的 Whisper 語音辨識技術，支援多種語言！

## ✨ 主要功能

- 支援多種音訊格式（mp3、wav、m4a、mov 等）
- 自動辨識中文內容
- 批次處理多個檔案
- 簡單易用的介面

## 🔧 安裝說明

### 1. 基本需求
- Python 3.8 或更新版本
- 音訊處理工具 ffmpeg

### 2. 安裝步驟

**第一步：下載專案**
```bash
git clone https://github.com/您的用戶名/您的專案名稱.git
cd 您的專案名稱
```

**第二步：設定虛擬環境**
```bash
# 建立虛擬環境
python3 -m venv whisper_env

# 啟動虛擬環境
# Windows 使用者請輸入：
whisper_env\Scripts\activate
# Mac/Linux 使用者請輸入：
source whisper_env/bin/activate
```

**第三步：安裝必要套件**
> 該步驟是安裝專案所需的套件
```bash
# 確保在虛擬環境中執行
pip3 install -r requirements.txt
```

**第四步：安裝 ffmpeg**
> 該工具是將音訊檔案轉換成文字的必要工具
> 如果已經安裝過 ffmpeg，可以跳過這一步
- Mac 使用者：
  ```bash
  brew install ffmpeg
  ```
- Windows 使用者：
  1. 前往 [ffmpeg 下載頁面](https://ffmpeg.org/download.html)
  2. 下載並安裝
- Linux 使用者：
  ```bash
  sudo apt-get install ffmpeg
  ```

## 🎯 使用方法

1. 把想要轉換的音訊檔案放到 `audio_files` 資料夾
2. 打開終端機，確保在虛擬環境中
3. 執行程式：
   ```bash
   python3 main.py
   ```
4. 等待處理完成，轉換好的文字檔會出現在 `transcripts` 資料夾

## ⚙️ 自訂設定

在 `main.py` 開頭的使用者設定區域，您可以修改：

1. 模型大小 (MODEL_SIZE)：
   - "tiny": 最快但準確度較低
   - "base": 平衡速度和準確度
   - "small": 較好的準確度
   - "medium": 更好的準確度
   - "large": 最佳準確度但最慢

2. 語言模式 (LANGUAGE_MODE)：
   - "zh": 純中文模式
   - "zh-en": 中英混合模式
   - "en": 純英文模式
   - "ja": 純日文模式

範例：
```python
# 設定為英文模式
LANGUAGE_MODE = "en"

# 設定為較大的模型
MODEL_SIZE = "medium"
```

## 使用完畢

```bash
# 關閉虛擬環境
deactivate
```

## 📁 資料夾說明

- `audio_files`: 放入要轉換的音訊檔案 (可一次處理多個檔案)
- `transcripts`: 程式會將轉換好的文字檔案存在這裡
- `whisper_cache`: 模型檔案的暫存區

## 💡 小提醒

- 第一次執行時會自動下載 Whisper 模型，需要一點時間
- 檔案越大，處理時間越長，請耐心等待
- 建議使用虛擬環境，避免套件版本衝突
- 如果音訊品質好，轉換結果會更準確

## 🎵 支援的檔案格式

- 音訊檔：`.mp3`、`.wav`、`.m4a`、`.flac`
- 影片檔：`.mov`、`.mp4`、`.m4v`

## ❓ 常見問題

**Q: 為什麼第一次執行特別慢？**
> A: 因為需要下載 Whisper 模型，只有第一次會比較慢。

**Q: 可以一次處理多個檔案嗎？**
> A: 可以！只要把所有檔案都放在 `audio_files` 資料夾即可。

**Q: 轉換品質不好怎麼辦？**
> A: 可以試試看：
    > 1. 確保音訊品質清晰
    > 2. 降低背景噪音
    > 3. 使用較大的模型（在程式碼中將 "base" 改為 "small" 或 "medium"）

## 📫 需要協助？

> 如果您遇到任何問題，歡迎：
    > 1. 在 GitHub 上開 Issue
    > 2. 寄信給我：sunny96087@yahoo.com.tw
    > 3. 查看 [OpenAI Whisper](https://github.com/openai/whisper) 官方文件

## 📝 授權說明

MIT License

Copyright (c) 2024 2魚

此程式為開源軟體，您可以：
- ✅ 自由使用、修改和分享
- ✅ 將其用於個人或商業專案
- ✅ 以此為基礎開發新的專案

唯一的要求是：
- 在您的專案中保留原始的版權和許可聲明

本專案使用了 [OpenAI Whisper](https://github.com/openai/whisper) 技術，
特別感謝所有開源社群的貢獻者。