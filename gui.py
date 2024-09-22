import os
import threading
from tkinter import *
from yt_dlp import YoutubeDL
import subprocess

# Create a threading event to signal the end of the download
download_complete = threading.Event()

def download_playlist():
    def run_download():
        try:
            playlist_url = url_entry.get()
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join('downloads', '%(title)s.%(ext)s'),
                'ffmpeg_location': os.path.join(os.getcwd(), 'ffmpeg', 'bin'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([playlist_url])
            # Signal that the download is complete
            download_complete.set()
        except Exception as e:
            # Handle any exceptions and stop the spinner
            stop_spinner()
            status_label.config(text=f"Error: {str(e)}")
            download_complete.set()

    # Start the spinner and clear any previous error messages
    status_label.config(text="")
    download_complete.clear()  # Reset the event
    start_spinner()
    threading.Thread(target=run_download).start()

def start_spinner():
    global spinner_running
    spinner_running = True
    update_spinner()

def stop_spinner():
    global spinner_running
    spinner_running = False

def update_spinner():
    if spinner_running:
        current_text = status_label.cget("text")
        if len(current_text) < 3:
            status_label.config(text=current_text + ".")
        else:
            status_label.config(text="")
        # Continue the spinner until the download is complete
        if not download_complete.is_set():
            root.after(500, update_spinner)
        else:
            # Stop spinner and update the label when download is complete
            stop_spinner()
            status_label.config(text="Download Complete")
            open_button.config(state=NORMAL)

def open_downloads_folder():
    folder_path = os.path.join(os.getcwd(), 'downloads')
    if os.name == 'nt':  # Windows
        subprocess.Popen(f'explorer "{folder_path}"')
    elif os.name == 'posix':  # macOS or Linux
        subprocess.Popen(['open', folder_path])

# Set up the GUI
root = Tk()
root.title('YouTube Playlist Downloader')

# Set the custom icon (optional)
root.iconbitmap('download.ico')

url_label = Label(root, text='Enter YouTube Playlist URL:')
url_label.pack(pady=10)

url_entry = Entry(root, width=50)
url_entry.pack(padx=10, pady=15)

download_button = Button(root, text='Download', command=download_playlist)
download_button.pack(pady=20)

status_label = Label(root, text='')
status_label.pack(pady=10)

open_button = Button(root, text='Open Downloads Folder', command=open_downloads_folder, state=DISABLED)
open_button.pack(pady=10)

root.mainloop()
