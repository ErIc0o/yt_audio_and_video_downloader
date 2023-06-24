from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
import time
import os
from PIL import ImageTk, Image
from urllib.request import urlopen
import webbrowser
import pyperclip

root = Tk()
root.title("YouTube download")
root.geometry("500x650")
root.resizable(False, False)
root.config(background="silver")

# Variable to store video link
video_Link = StringVar()
# Variable to store download path
download_Path = StringVar()
# Variable to store video details
video_Title = StringVar()
video_Length = StringVar()
video_uploaded = StringVar()
video_Author = StringVar()

#using empty string for always clearing any data from clipboard first------
pyperclip.copy('')

#Function for Searching Query from YouTube---------
def yt():
    """
    Open a web browser with YouTube search results based on the query entered.
    """
    webbrowser.open_new(f'https://www.youtube.com/results?search_query={root.entry.get()}')
    reset_data()

#Function for pasteing data from clipboard to entry widget--------------------
def update_text_entry():
    """
    Update the text entry widget with the contents of the clipboard.
    """
    clipboard_data = pyperclip.paste()
    root.linkText.delete(0, tk.END)
    root.linkText.insert(0, clipboard_data)
    
    if clipboard_data.startswith("https://www.youtube.com/"):
        return
    
    root.after(100, update_text_entry)# Check every 100 milliseconds


#Function for reseting data from netry widget and clipboard-----------
def reset_data():
    """
    Reset the video link, video details, and download path.
    """
    root.linkText.delete(0, tk.END)
    
    pyperclip.copy('')
    update_text_entry()
    video_Title.set("")
    video_Length.set("")
    video_uploaded.set("")
    video_Author.set("")
    download_Path.set("")
    root.bar['value'] = 0
    root.percentage.configure(text="0%")
    root.percentage.update()

    


#Function for svaing video and audio to file manager-----------------
def Browse():
    """
    Open a file dialog to select the download destination folder.
    """
    download_Directory = filedialog.askdirectory()
    download_Path.set(download_Directory)


#Function for  video download--------------
def download_video():
    """
    Download the YouTube video based on the provided link, selected resolution, and download path.
    """
    details()
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    selected_resolution = resolution_combobox.get()
    getVideo = YouTube(Youtube_link, on_progress_callback=on_progress)

    videoStream = getVideo.streams.filter(progressive=True).order_by('resolution').desc()
    videoStreamr = videoStream.filter(res=selected_resolution).first()
    videoStreamr.download(download_Folder)

    messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_Folder)



#Function for details of video-------------
def details():
    """
    Fetch and display video details such as title, length, upload date, and author.
    """
    url = YouTube(str(video_Link.get()))

    try:
        
        video_Title.set(url.title)
        xx = time.strftime("%H:%M:%S", time.gmtime(url.length))
        video_Length.set(xx)
        video_uploaded.set(url.publish_date)
        video_Author.set(url.author)

        # Thumbnail
        thumbnail_url = url.thumbnail_url
        image = Image.open(urlopen(thumbnail_url))
        image = image.resize((150, 150), Image.ANTIALIAS)
        thumbnail = ImageTk.PhotoImage(image)

        #thumbnail label--------------
        thumbnail_label = Label(root, image=thumbnail)
        thumbnail_label.place(x=320, y=300)
        #adding thumbnail to label---------
        thumbnail_label.image = thumbnail

    except:
        messagebox.showerror("Link Error", "Please paste a YouTube link")
        

    # Labels for details
    Lbl = Label(root, text="Video Title-", font="san-serif 14 bold")
    Lbl.place(x=0, y=230)
    Lbl = Label(root, text="", textvariable=video_Title)
    Lbl.place(x=0, y=270)
    Lbl = Label(root, text="Video Length-", font="san-serif 14 bold")
    Lbl.place(x=0, y=310)
    Lbl = Label(root, text="", textvariable=video_Length)
    Lbl.place(x=0, y=350)
    Lbl = Label(root, text="Video Uploaded-", font="san-serif 14 bold")
    Lbl.place(x=0, y=390)
    Lbl = Label(root, text="", textvariable=video_uploaded)
    Lbl.place(x=0, y=430)
    Lbl = Label(root, text="Video Creator-", font="san-serif 14 bold")
    Lbl.place(x=0, y=470)
    Lbl = Label(root, text="", textvariable=video_Author)
    Lbl.place(x=0, y=510)

#Function for download progress----------------
def on_progress(stream, chunk, bytes_remaining):
    """
    Callback function for the download progress.
    Update the progress bar and percentage label.
    """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = int((bytes_downloaded / total_size) * 100)
    per = str(percentage_of_completion)
    root.percentage.configure(text=per + "%")
    root.percentage.update()
    root.bar['value'] = percentage_of_completion
    root.update_idletasks()


#Function for audio download-------------------
def Download_audio():
    """
    Download the audio of the YouTube video based on the provided link and download path.
    """
    details()
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getaudio = YouTube(Youtube_link, on_progress_callback=on_progress)
    videoStream = getaudio.streams.filter(only_audio=True).first()
    out_file = videoStream.download(download_Folder)
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3 "
    os.rename(out_file, new_file)

    messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_Folder)



# Label
head_label = Label(root, text="YouTube Audio/Video Downloader", font="Arial 14", fg="black", bg="gray")
head_label.place(x=90, y=0)

link_label = Label(root, text="Query:", bd=3, height=1, bg="gray")
link_label.place(x=0, y=33)

link_label = Label(root, text="YouTube link:", bd=3, height=1, bg="gray")
link_label.place(x=0, y=63)

destination_label = Label(root, text="Destination:", bd=3, height=1, bg="gray")
destination_label.place(x=0, y=93)

# Progress Bar
root.bar = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
root.bar.place(x=100, y=600)

# Percentage Label
root.percentage = Label(root, text="0%")
root.percentage.place(x=420, y=600)

# Entry widget for video link
root.entry = Entry(root, width=27, font="Arial 14")
root.entry.place(x=90, y=30)

# Entry widget for YouTube link
root.linkText = Entry(root, width=35, textvariable=video_Link, font="Arial 14")
root.linkText.place(x=90, y=60)

# Entry widget for download destination
root.destinationText = Entry(root, width=27, textvariable=download_Path, font="Arial 14")
root.destinationText.place(x=90, y=90)

# Browse button
browse_B = Button(root, text="Browse", command=Browse, width=10, bg="gray", relief=GROOVE)
browse_B.place(x=400, y=90)

# Download Video button
download_button = Button(root, text="Download Video", command= download_video, width=20, bg="red", relief=GROOVE, font="Georgia, 13")
download_button.place(x=70, y=130)  

# Combobox for selecting video resolution
resolution_combobox = ttk.Combobox(root, state="readonly", width=3,font="Georgia, 13")
resolution_combobox['values'] = ("1080p" ,"720p","480p","360p","240p","144p")
resolution_combobox.set("720p")
resolution_combobox.place(x=7, y=135)

# Download Audio button
Download_aB2 = Button(root, text="Download Audio", command=Download_audio, width=20, bg="red", relief=GROOVE, font="Georgia, 13")
Download_aB2.place(x=270, y=130)

# Search button
Search_sB3 = Button(root, text="Search", command=yt, width=10, bg="gray", relief=GROOVE)
Search_sB3.place(x=400, y=30)

# Download_sB3 = Button(root, text="check", command=details, width=5)
# Download_sB3.place(x=400, y=600)

update_text_entry()

root.mainloop()

