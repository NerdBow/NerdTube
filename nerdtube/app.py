import customtkinter
from selected_video_frame import SelectedVideoFrame
from search_frame import SearchFrame


class App(customtkinter.CTk):
    NAME = "NerdTube"

    WIDTH = 800
    HEIGHT = 800

    def __init__(self):
        super().__init__()

        self.title(self.NAME)
        self.geometry(f"{self.HEIGHT}x{self.WIDTH}")
        self.minsize(self.WIDTH, self.HEIGHT)
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1), weight=1)
        self.search_frame = SearchFrame(self)
        self.search_frame.grid(row=0, column=0, padx=20, pady=20, columnspan=2, rowspan=2, sticky="nwes")

        self.selected_video_frame = SelectedVideoFrame(self)
        self.selected_video_frame.grid(row=0, column=2, padx=20, pady=20, columnspan=1, sticky="nwes")

        self.bind("<Configure>", self.resize)

    def setup(self):
        """
        Method to run any code that needs to be executed after instaciation of the instance
        """
        self.search_frame.setup(self.selected_video_frame)
        # self.selected_video_frame.setup()

    def resize(self, event):
        """
        Method which is called when the window is resized
        """
        self.search_frame.video_display_frame.resize_images()
        print("Resizing...")


if __name__ == "__main__":
    app = App()
    app.update()
    app.setup()
    app.mainloop()
