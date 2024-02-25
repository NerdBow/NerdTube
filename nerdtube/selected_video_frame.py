import customtkinter as ctk

from nerdtube.video_frame import VideoFrame


class SelectedVideoFrame(ctk.CTkFrame):
    """
    Displays meta data about selected video from VideoDisplayFrame
    """

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(master=master)

        self._font = ctk.CTkFont(family="Roboto", size=20, weight="bold")

        self._selected_video: VideoFrame = None

        self.columnconfigure((0), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)

        self._heading_label = ctk.CTkLabel(master=self, text="Selected Video", font=self._font)
        self._heading_label.grid(row=0, column=0, sticky="nsew")

        self._thumbnail_label = ctk.CTkLabel(master=self, text="")
        self._thumbnail_label.grid(row=1, column=0, rowspan=5, sticky="nsew")

        self._video_title_label = ctk.CTkLabel(
            master=self, text="Video Title:", anchor="w", font=self._font, wraplength=200
        )
        self._video_title_label.grid(row=7, column=0, sticky="ew")

        self._video_length_label = ctk.CTkLabel(
            master=self, text="Video Length:", anchor="w", font=self._font
        )
        self._video_length_label.grid(row=8, column=0, sticky="ew")

    def set_video_info(self) -> None:
        """
        Set the frame's labels on video infomation to those of the selected_video attribute
        """
        self._thumbnail_label.configure(image=self._selected_video.thumbnail_image)
        self._video_title_label.configure(text=self._selected_video.youtube_object.title)
        self._video_length_label.configure(
            text=f"{(self._selected_video.youtube_object.length // 3600):02d}:{((self._selected_video.youtube_object.length % 3600) // 60):02d}:{((self._selected_video.youtube_object.length % 3600) % 60):02d}"
        )

    @property
    def selected_video(self) -> VideoFrame:
        return self._selected_video

    @selected_video.setter
    def selected_video(self, value) -> None:
        self._selected_video = value
