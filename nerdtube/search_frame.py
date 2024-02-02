import customtkinter
from pytube import Search
from nerdtube.video_display_frame import VideoDisplayFrame


class SearchFrame(customtkinter.CTkFrame):
    """
    Frame to handle a search bar and search results
    """

    def __init__(self, master: customtkinter.CTk) -> None:
        super().__init__(master)

        self.master = master

        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0), weight=0)
        self.grid_rowconfigure((1), weight=1)

        self.search_bar = customtkinter.CTkEntry(master=self, placeholder_text="Search", height=32)
        self.search_bar.grid(row=0, column=0, padx=20, pady=20, sticky="new")
        self.search_bar.bind("<Return>", command=self.search)

        self.video_display_frame = VideoDisplayFrame(master=self)
        self.video_display_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    def setup(self):
        self.video_display_frame.setup_image_dimensions()

    def search(self, event) -> None:
        """
        Function which is called when Enter is pressed on the search bar
        Take current text in search bar and puts it through Pytube Search object

        Parameters:
        - event: event object for the search command (I never used it)
        """

        search_query = self.search_bar.get()

        if search_query == "":
            return

        search_object = Search(search_query)

        self.video_display_frame.delete_videos()
        self.video_display_frame.add_videos(videos=search_object.results)

        print(f"Searching...\n{self.search_bar.get()}")
        print(f"{search_object.results}")
        print(f"Size: {len(search_object.results)}")
