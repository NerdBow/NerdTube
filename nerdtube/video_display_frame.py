import customtkinter as ctk
from pytube import YouTube
from PIL import Image
from urllib.request import urlopen


class VideoDisplayFrame(ctk.CTkScrollableFrame):
    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        self.image_width = 0
        self.image_height = 0

        self.video_images = []
        self.video_frames = []

    def setup_image_dimensions(self):
        """
        Setups the image dimensions for the thumbnails of videos depending on the window size
        """

        # Math to fit the 3 videos per row to scale with the size of the screen
        self.image_width = self.winfo_width() // 3

        # Makes sure that the image is 16:9
        self.image_height = self.image_width // 16 * 9

        print(f"Width: {self.winfo_width()} Height: {self.winfo_height()}")

    def resize_images(self):
        """
        Resizes the images of video thumbnails depending on the screen size
        """
        # Only scales if there is a 10 pixel difference in the window difference
        if abs(self.image_width - self.winfo_width() // 3) < 25:
            return

        self.setup_image_dimensions()

        for video in self.video_images:
            video.cget("image").configure(size=(self.image_width, self.image_height))

    def on_video_click(self, event, video_frame: ctk.CTkFrame):
        """
        Highlight video frame when the thumbnail is clicked

        Parameters:
        - event: The event object
        - video_frame: The video frame of the clicked thumbnail
        """

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
            video_frame = ctk.CTkFrame(master=self, border_width=2, border_color="white")

            image = Image.open(urlopen(video.thumbnail_url))  # Troll
            image_ctk = ctk.CTkImage(
                light_image=image, dark_image=image, size=(self.image_width, self.image_height)
            )
            thumbnail_label = ctk.CTkLabel(master=video_frame, image=image_ctk, text="")
            thumbnail_label.grid(row=0, column=0, padx=2, pady=2)

            title_label = ctk.CTkLabel(
                master=video_frame, text=video.title, wraplength=180
            )
            title_label.grid(row=1, column=0, padx=2, pady=2)

            video_frame.grid(row=index // 3, column=index % 3, padx=5, pady=5)
            print(f"Row: {index // 3} | Column: {index % 3}")

            self.video_images.append(thumbnail_label)
            self.video_frames.append(video_frame)

            thumbnail_label.bind(
                "<Button-1>",
                command=lambda event, frame=video_frame: self.on_video_click(event, frame),
            )

    def delete_videos(self) -> None:
        """
        Deletes all the videos label objects within a frame
        """
        for video in self.video_frames:
            video.destroy()
