from os import link
from pytube import YouTube
import os

class Downloader:

    def __init__(self, link_video, save_path, video_format):
        self.link_video = link_video
        self.save_path = save_path
        self.video_format = video_format
        
    def save_video(self):
        # If the Instanciation of the class fail, it's because the URL is not available
        try:  
            yt = YouTube(self.link_video)  
        except: 
            # So we return the error message
            return "ERROR : WRONG OR EMPTY LINK"

        # The download can fail, for example, if the internet connexion is turned off during the download
        try:
            # Maybe here, we can had the possibility to change the video resolution
            if self.video_format == "mp4":
                yt.streams.filter(progressive=True, file_extension=self.video_format).get_by_resolution("720p").download(self.save_path)
            else:
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(self.save_path)
                # save the file
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
        except:
            return "ERROR : CONNEXION"

        # Return 0 = succeed, and the youtube object to get all informations on the video
        return 0, yt




