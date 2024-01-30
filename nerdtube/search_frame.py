import customtkinter
from pytube import Search, YouTube
from PIL.Image import Image
from urllib.request import urlopen

class SearchFrame(customtkinter.CTkFrame):
    """
    Frame to handle a search bar and search results
    """
    def __init__(self, master: customtkinter.CTk) -> None:
        super().__init__(master)
        self.search_results = []
        self.current_row = 0
        self.current_column = 0


        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0), weight=1)

        self.search_bar = customtkinter.CTkEntry(master=self, placeholder_text="Search", height=32)
        self.search_bar.grid(row=0, column=0, padx=20, pady=20, sticky="new")

        self.search_bar.bind("<Return>", command=self.search)
        pass

    def search(self, event):
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

        print(f"Searching...\n{self.search_bar.get()}")
        print(f"{search_object.results}")

    def append_result(self, result_object: YouTube) -> None:
        """
        Appends a search result to the search results list of the frame.

        Parameters:
        - result_object: The youtube object to append to the results list
        """

        image = Image(urlopen(result_object.thumbnail_url))
        image_widget = customtkinter.CTkImage(light_image=image, dark_image=image, size=(80, 45))

        label_widget = customtkinter.CTkLabel(master=self, image=image_widget, text=result_object.title)

        self.search_results.append(label_widget)

