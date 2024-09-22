import os
from yt_dlp import YoutubeDL

def download_and_convert_to_mp3(video_url, download_folder, ffmpeg_location=None):
    try:
        # Set up yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # Optionally, provide the ffmpeg path if not in system PATH
        if ffmpeg_location:
            ydl_opts['ffmpeg_location'] = ffmpeg_location

        # Download audio
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        print(f"Downloaded and converted: {video_url}")
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")

def download_playlist_to_mp3(playlist_url, download_folder='downloads', ffmpeg_location=None):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Download the entire playlist
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    if ffmpeg_location:
        ydl_opts['ffmpeg_location'] = ffmpeg_location

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == '__main__':
    playlist_url = input("Enter the YouTube playlist URL: ")
    # Optionally, provide the path to ffmpeg binary if it's not in the system PATH
    # Example: ffmpeg_location='C:/path/to/ffmpeg/bin'
    download_playlist_to_mp3(playlist_url, ffmpeg_location='C:/Users/Abhash/Downloads/ffmpeg/bin')
