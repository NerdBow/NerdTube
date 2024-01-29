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

        self.search_bar = customtkinter.CTkEntry(master=self, placeholder_text="Search")
        self.search_bar.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=3, rowspan=3)
        pass

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

