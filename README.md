# YTVD (YouTube Video Downloader)

A modern, sleek GUI-based YouTube Video Downloader built using Python, `CustomTkinter`, and `yt-dlp`.

> **Note for Non-Python Users:**  
> If you don't have Python installed and want a standalone Windows executable (`.exe`), download the compiled installer here:
>
> 📥 **[Download YTVD Setup (v2.0.0)](https://github.com/hollowstride/YTVD/releases/download/v2.0.0/YTVD_Setup.exe)**

> **Disclaimer:** This application is strictly designed and tested **only for Windows OS**.

---

## ⭐ Support

If you find YTVD useful, consider giving the repository a ⭐ on GitHub!

**Made with 💗 using Python, CustomTkinter, and yt-dlp.**

---

## Features

- **Standalone Setup:** Automatic dependency checks—no Python or FFmpeg manual setup required when using the `.exe` installer.
- **Modern Dark UI:** Responsive interface powered by `CustomTkinter`.
- **Non-Blocking GUI:** Uses background threading for smooth downloading without UI freezing.
- **Real-Time Progress:** Live progress bar and status updates.
- **Quality Options:** Select between `Highest`, `1080p`, `720p`, and `480p`.
- **Auto-MP4 Remux:** Automatically merges audio and video into `.mp4`.
- **Direct Save:** Downloads are automatically saved to your system's `Downloads` folder.

---

## Requirements (Source Code Only)

*If you are running the pre-compiled installer (`YTVD_Setup.exe`), you can skip this section.*

- **Windows OS**
- **Python 3.8+**
- **FFmpeg** (Required for merging video & audio streams)

### Installing Python Dependencies

```bash
pip install customtkinter yt-dlp
```

### Installing FFmpeg (Required for running from source)

Install via Windows Command Prompt:

```cmd
winget install FFmpeg
```

Make sure `ffmpeg` is added to your system `PATH`.

---

## How to Run from Source

```bash
python main.py
```

1. Paste your YouTube video link.
2. Select your preferred resolution.
3. Click **Start Download**.
4. Your file will be saved to your **Downloads** folder.

---

## License

Use and distribute this project according to the license included in the repository.
