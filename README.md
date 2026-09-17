# YTVD (YouTube Video Downloader)

A modern, sleek GUI-based YouTube Video Downloader built using Python, `CustomTkinter`, and `yt-dlp`.

> **Note for Non-Python Users:**  
> If you don't have Python installed and want a standalone Windows executable (`.exe`), download the compiled version here: **[INSERT LINK HERE]**

> **Disclaimer:** This application is strictly designed and tested **only for Windows OS**.

---

## Features
- **Modern Dark UI:** Responsive interface powered by `CustomTkinter`.
- **Non-Blocking GUI:** Uses background threading for smooth downloading without UI freezing.
- **Real-Time Progress:** Live progress bar and status updates.
- **Quality Options:** Select between `Highest`, `1080p`, `720p`, and `480p`.
- **Auto-MP4 Remux:** Automatically merges audio and video into `.mp4`.
- **Direct Save:** Downloads are automatically saved to your system's `Downloads` folder.

---

## Requirements

- **Windows OS**
- **Python 3.8+**
- **FFmpeg** (Required for merging video & audio streams)

### Installing Python Dependencies
```bash
pip install customtkinter yt-dlp
```

### Installing FFmpeg (Required)
Install via Windows Command Prompt:
```cmd
winget install FFmpeg
```
*(Make sure `ffmpeg` is added to your System PATH).*

---

## How to Run

```bash
python main.py
```

1. Paste your YouTube video link.
2. Select your preferred resolution.
3. Click **Start Download**. Your file will be saved in your **Downloads** folder.
