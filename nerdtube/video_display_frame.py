import customtkinter as ctk
from pytube import YouTube
from PIL import Image
from urllib.request import urlopen

from nerdtube.video_frame import VideoFrame


class VideoDisplayFrame(ctk.CTkScrollableFrame):
    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        self.video_images = []
        self.video_frames = []

    def setup_image_dimensions(self):
        """
        Setups the image dimensions for the thumbnails of videos depending on the window size
        """

        # Math to fit the 3 videos per row to scale with the size of the screen
        VideoFrame.image_width = self.winfo_width() // 3

        # Makes sure that the image is 16:9
        VideoFrame.image_height = VideoFrame.image_width // 16 * 9

        print(f"Width: {self.winfo_width()} Height: {self.winfo_height()}")

    def resize_images(self):
        """
        Resizes the images of video thumbnails depending on the screen size
        """
        # Only scales if there is a 25 pixel difference in the window difference
        if abs(VideoFrame.image_width - self.winfo_width() // 3) < 25:
            return

        self.setup_image_dimensions()

        for image_label in self.video_images:
            image_label.cget("image").configure(
                size=(VideoFrame.image_width, VideoFrame.image_height)
            )

    def on_video_click(self, event, video_frame: ctk.CTkFrame):
        """
        Highlight video frame when the thumbnail is clicked

        Parameters:
        - event: The event object
        - video_frame: The video frame of the clicked thumbnail
        """

        print(video_frame)
        for frame in self.video_frames:
            frame.configure(border_color="white")

        video_frame.configure(border_color=("#5CEEFF"))
        print(event)
        print(video_frame.winfo_children()[1].cget("text"))

    def add_videos(self, videos: list[YouTube]) -> None:
        """
        Creates labels for each video in the videos list and ands them to the frame

        Parameters:
        - videos: List of Youtube objects
        """

        self.setup_image_dimensions()

        for index, video in enumerate(videos):
            video_frame = VideoFrame(master=self, youtube_object=video)

            video_frame.grid(row=index // 3, column=index % 3, padx=5, pady=5)
            print(f"Row: {index // 3} | Column: {index % 3}")

            self.video_images.append(video_frame.thumbnail_label)
            self.video_frames.append(video_frame)

            video_frame.thumbnail_label.bind(
                "<Button-1>",
                command=lambda event, frame=video_frame: self.on_video_click(event, frame),
            )

    def delete_videos(self) -> None:
        """
        Deletes all the videos label objects within a frame
        """
        for video in self.video_frames:
            video.thumbnail_label.unbind("<Button-1>")
            video.destroy()
        self.video_frames.clear()
        self.update()
