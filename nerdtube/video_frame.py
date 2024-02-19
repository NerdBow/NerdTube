import customtkinter as ctk
from pytube import Youtube
from PIL import Image
from urllib.request import urlopen


class VideoFrame(ctk.CTkFrame):
    """
    Frame which contains all the information about a youtube vidoe including GUI data
    """

    def __init__(self, video_display_frame: ctk.CTkFrame, youtube_object: Youtube) -> None:
        super.__init__(master=video_display_frame, border_width=2, border_color="white")
        image = Image.open(urlopen(youtube_object.thumbnail_url))
        self.youtube_object = youtube_object
        pass
