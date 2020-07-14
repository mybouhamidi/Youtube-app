from pytube import YouTube
from pytube import Playlist
import os, sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def start():
    #Input 
    global file_size
    case = input("You want to download a playlist/video (P/V): ")
    if (case.upper()=='P'):
        yt_url = input("Copy and paste your YouTube URL here: ")
        print(yt_url)
        print ("Accessing YouTube URL...")
        try:
            playlist = Playlist(yt_url)
        except:
            print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
            redo = start()

        #Starts the download process
        for video in playlist:
            yt = YouTube(video)
            yt_type = yt.streams.filter(progressive = True, file_extension = "mp4").first()

        #Gets the title of the video
            title = yt.title

        #Prepares the file for download
            print ("Fetching: {}...".format(title))
        
        #Starts the download process
            yt_type.download()
        print ("Ready to download again.\n\n")
        again = start()
    # Searches for the video and sets up the callback to run the progress indicator. 
    elif (case.upper()=='V'):  
        yt_url = input("Copy and paste your YouTube URL here: ")
        print(yt_url)
        print ("Accessing YouTube URL...") 
        try:
            video = YouTube(yt_url)
        except:
            print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
            redo = start()
        #Get the first video type - usually the best quality.
        video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()

        #Gets the title of the video
        title = video.title

        #Prepares the file for download
        print ("Fetching: {}...".format(title))
        
        #Starts the download process
        video_type.download()
        print ("Ready to download again.\n\n")
        again = start()
    else:
        print('A ZMER follow the given values')
        redo = start()
    

begin = start()