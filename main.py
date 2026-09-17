import os
import threading
from tkinter import filedialog, messagebox
import customtkinter as ctk
import yt_dlp

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class YouTubeDownloader(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("YouTube Video Downloader")
        self.geometry("600x450")
        self.minsize(500, 400)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Card Container Frame
        self.card_frame = ctk.CTkFrame(
            self, corner_radius=16, fg_color="#112240", border_width=1, border_color="#233554"
        )
        self.card_frame.grid(row=0, column=0, padx=24, pady=24, sticky="nsew")
        self.card_frame.grid_columnconfigure(0, weight=1)

        # Header Section
        self.title_label = ctk.CTkLabel(
            self.card_frame, text="YouTube Downloader", font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color="#F8FAFC"
        )
        self.title_label.grid(row=0, column=0, sticky="w", padx=24, pady=(24, 4))

        self.subtitle_label = ctk.CTkLabel(
            self.card_frame, text="Paste your video link below to begin", font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#8892B0"
        )
        self.subtitle_label.grid(row=1, column=0, sticky="w", padx=24, pady=(0, 20))

        # URL Input Field
        self.url_label = ctk.CTkLabel(
            self.card_frame, text="VIDEO URL", font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
            text_color="#8892B0"
        )
        self.url_label.grid(row=2, column=0, sticky="w", padx=24, pady=(0, 4))

        self.url_entry = ctk.CTkEntry(
            self.card_frame,
            placeholder_text="https://youtu.be/...",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            fg_color="#0A192F",
            border_color="#233554",
            text_color="#F8FAFC",
            height=40,
            corner_radius=8,
        )
        self.url_entry.grid(row=3, column=0, sticky="ew", padx=24, pady=(0, 16))

        # Quality Selector
        self.quality_label = ctk.CTkLabel(
            self.card_frame,
            text="PREFERRED QUALITY",
            font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
            text_color="#8892B0",
        )
        self.quality_label.grid(row=4, column=0, sticky="w", padx=24, pady=(0, 4))

        self.quality_var = ctk.StringVar(value="Highest")
        self.quality_menu = ctk.CTkOptionMenu(
            self.card_frame,
            values=["Highest", "1080p", "720p", "480p"],
            variable=self.quality_var,
            font=ctk.CTkFont(family="Segoe UI", size=13),
            dropdown_font=ctk.CTkFont(family="Segoe UI", size=12),
            fg_color="#0A192F",
            button_color="#1E3A8A",
            button_hover_color="#2563EB",
            text_color="#F8FAFC",
            dropdown_fg_color="#0A192F",
            dropdown_text_color="#F8FAFC",
            dropdown_hover_color="#1E3A8A",
            height=40,
            corner_radius=8,
        )
        self.quality_menu.grid(row=5, column=0, sticky="ew", padx=24, pady=(0, 20))

        # Progress Bar
        self.progress_bar = ctk.CTkProgressBar(self.card_frame, height=8, corner_radius=4)
        self.progress_bar.grid(row=6, column=0, sticky="ew", padx=24, pady=(0, 16))
        self.progress_bar.set(0)

        # Download Button
        self.download_button = ctk.CTkButton(
            self.card_frame,
            text="Start Download",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            height=42,
            corner_radius=8,
            command=self.download_video,
        )
        self.download_button.grid(row=7, column=0, sticky="ew", padx=24, pady=(0, 12))

        # Status Output Label
        self.status_label = ctk.CTkLabel(
            self.card_frame, text="Ready", font=ctk.CTkFont(family="Segoe UI", size=12), text_color="#8892B0"
        )
        self.status_label.grid(row=8, column=0, pady=(0, 16))

    def download_video(self):
        video_url = self.url_entry.get().strip()
        if not video_url:
            messagebox.showerror("Error", "Please enter a valid YouTube URL.")
            return

        quality = self.quality_var.get()
        self.set_ui_state(downloading=True)
        self.progress_bar.set(0)

        threading.Thread(target=self.perform_download, args=(video_url, quality), daemon=True).start()

    def _progress_hook(self, d):
        if d.get("status") == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
            downloaded = d.get("downloaded_bytes", 0)
            if total > 0:
                progress = downloaded / total
                self.after(0, lambda: self.progress_bar.set(progress))

    def perform_download(self, video_url, quality):
        try:
            # Drop format restrictions so yt_dlp can select best quality WebM/VP9 streams,
            # then let merge_output_format remux it to MP4.
            if quality == "Highest":
                format_opt = "bestvideo+bestaudio/best"
            else:
                res = quality.replace("p", "")
                format_opt = f"bestvideo[height<={res}]+bestaudio/best[height<={res}]/best"

            ydl_opts = {
                "format": format_opt,
                "outtmpl": os.path.join(os.path.expanduser("~/Downloads"), "%(title)s.%(ext)s"),
                "merge_output_format": "mp4",
                "noplaylist": True,  # Ensures single-video downloads
                "progress_hooks": [self._progress_hook],
                "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
            }

            self.after(0, lambda: self.update_status("Fetching metadata...", "#60A5FA"))

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=True)
                title = info.get("title", "Video")

                self.after(0, lambda: self.progress_bar.set(1.0))
                self.after(0, lambda: self.update_status(f"Saved: {title}", "#34D399"))
                self.after(0, lambda: messagebox.showinfo("Success", f"Video '{title}' downloaded successfully!"))
                self.after(0, lambda: self.url_entry.delete(0, "end"))

        except Exception as e:
            err_msg = str(e)
            self.after(0, lambda: self.update_status("Download failed!", "#F87171"))

            # Specific warning if FFmpeg is missing on Windows
            if "ffmpeg" in err_msg.lower():
                self.after(
                    0,
                    lambda: messagebox.showerror(
                        "FFmpeg Missing",
                        "FFmpeg was not found on your system PATH.\nPlease install FFmpeg to allow format merging."
                    )
                )
            else:
                self.after(0, lambda: messagebox.showerror("Error", f"Download failed.\n{err_msg}"))
        finally:
            self.after(0, lambda: self.set_ui_state(downloading=False))

    def update_status(self, text, color):
        self.status_label.configure(text=text, text_color=color)

    def set_ui_state(self, downloading):
        if downloading:
            self.download_button.configure(state="disabled", text="Downloading...", fg_color="#1E293B")
        else:
            self.download_button.configure(state="normal", text="Start Download", fg_color="#2563EB")


if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()
