import customtkinter
from pytube import YouTube
from PIL import Image
from urllib.request import urlopen


class VideoDisplayFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master: customtkinter.CTkFrame) -> None:
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        self.image_width = 0
        self.image_height = 0

        self.video_images = []
        self.video_labels = []

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
        # Only scales if there is a 10 pixel difference in the window difference
        if abs(self.image_width - self.winfo_width() // 3) < 25:
            return

        self.setup_image_dimensions()

        for video in self.video_labels:
            video.cget("image").configure(size=(self.image_width, self.image_height))

    def add_videos(self, videos: list[YouTube]) -> None:
        """
        Creates labels for each video in the videos list and ands them to the frame

        Parameters:
        - videos: List of Youtube objects
        """

        self.setup_image_dimensions()

        for index, video in enumerate(videos):
            video_frame = customtkinter.CTkFrame(master=self)

            image = Image.open(urlopen(video.thumbnail_url))  # Troll
            image_ctk = customtkinter.CTkImage(
                light_image=image, dark_image=image, size=(self.image_width, self.image_height)
            )
            label = customtkinter.CTkLabel(master=video_frame, image=image_ctk, text="")
            label.grid(row=0, column=0, padx=2, pady=2)

            title_label = customtkinter.CTkLabel(
                master=video_frame, text=video.title, wraplength=180
            )
            title_label.grid(row=1, column=0, padx=2, pady=2)

            video_frame.grid(row=index // 3, column=index % 3, padx=5, pady=5)
            print(f"Row: {index // 3} | Column: {index % 3}")
            self.video_labels.append(label)

    def delete_videos(self) -> None:
        """
        Deletes all the videos label objects within a frame
        """
        for video in self.video_labels:
            video.destroy()
