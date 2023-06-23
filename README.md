# YT Audio and Video Downloader
This is a Python script that allows you to download YouTube videos and extract audio from them using the PyTube library. The script provides a graphical user interface (GUI) built with the Tkinter library.

# Prerequisites
Before running the script, make sure you have the following libraries installed:

tkinter
pytube
PIL (Python Imaging Library)
pyperclip
You can install these libraries using pip:

Copy code
pip install tkinter pytube pillow pyperclip

# Usage
Run the script using the command python youtube_downloader.py.
The GUI window will open.
Enter a search query in the "Query" field or directly paste a YouTube link in the "YouTube link" field.
Click the "Search" button to open a web browser with YouTube search results based on the query entered.
Click the "Download Video" button to download the video. You can select the desired video resolution from the drop-down menu.
Click the "Download Audio" button to extract audio from the video and save it as an MP3 file.
Click the "Browse" button to choose the download destination folder.
The progress bar will show the download progress, and the percentage label will display the current progress percentage.
Once the download is complete, a message box will appear showing the download path.
The video details such as title, length, upload date, and author will be displayed below the buttons.
The video thumbnail will be displayed on the right side of the window.
Note: The script supports downloading videos in resolutions of 720p and 360p. You can modify the available resolutions by editing the values attribute of the resolution_combobox variable.

# License
This script is licensed under the MIT License. Feel free to modify and distribute it according to your needs.

# Disclaimer
This script is intended for personal use only. Please respect the YouTube terms of service and the rights of content creators when using this script.
