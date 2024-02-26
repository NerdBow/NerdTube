import customtkinter as ctk
from pytube import YouTube
from PIL import Image
from urllib.request import urlopen


class VideoFrame(ctk.CTkFrame):
    """
    Frame which contains all the information about a youtube vidoe including GUI data
    """

    image_width = 0
    image_height = 0

    def __init__(self, master: ctk.CTkFrame, youtube_object: YouTube) -> None:
        super().__init__(master=master, border_width=2, border_color="white")

        self.youtube_object = youtube_object

        thumbnail = Image.open(urlopen(youtube_object.thumbnail_url))
        self.thumbnail_image = ctk.CTkImage(
            light_image=thumbnail,
            dark_image=thumbnail,
            size=(VideoFrame.image_width, VideoFrame.image_height),
        )

        self.thumbnail_label = ctk.CTkLabel(master=self, image=self.thumbnail_image, text="")
        self.thumbnail_label.grid(row=0, column=0, padx=2, pady=2)

        self.title_label = ctk.CTkLabel(master=self, text=self.youtube_object.title, wraplength=180)
        self.title_label.grid(row=1, column=0, padx=2, pady=2)
