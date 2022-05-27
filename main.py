import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from python_classes.downloader import Downloader


kivy.require('2.1.0')

class Interface(Widget):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Default value of the format (mp3 or mp4 only)
        self.format = "mp4"

    def on_button_submit(self):
        # Input who contains the url of the video
        input = self.ids.text_input_url
        # Call the downloader with the URL, the save path and the format        
        downloader = Downloader(input.text, self.ids.text_input_path.text, self.format)
        # Saving the video
        return_downloader = downloader.save_video()
        # If return code is not 0 (error)
        if return_downloader[0] != 0:
            # Get the error message and set the color of the status label to red
            self.ids.status.text = return_downloader
            self.ids.status.color = (1, 0, 0, 1)
        else:
            # Print that the download as succeed and set the color of the status label to green
            self.ids.status.text = f"Video successfully downloaded"
            self.ids.status.color = (0, 1, 0, 1)
        # Reset the URL
        input.text = ""

        # Maybe here we can call a function self.show_video_resume who shows on the application the resume
        # of the video who has been downloaded (tile, description, etc). All this informations are in the
        # YouTube object => return_downloader[1]


    """def show_video_resume(self):
        pass"""

    def on_button_format(self):
        # Button who allows the user to change the video format
        button = self.ids.button_format
        # Swap between the 2 values
        if self.format == "mp4":
            self.format = "mp3"
            button.text = "MP3"
        else:
            self.format = "mp4"
            button.text = "MP4"

    
class YoutubeDownloaderApp(App):
    pass

YoutubeDownloaderApp().run()