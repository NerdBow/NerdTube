import customtkinter
from search_frame import SearchFrame

class App(customtkinter.CTk):
    NAME = "NerdTube"

    def __init__(self):
        super().__init__()
        self.title(self.NAME)
        self.geometry("800x800")
        self.search_frame = SearchFrame(self)
        self.search_frame.grid(row=0, column=0, padx=20, pady=20, rowspan=10, columnspan=10)
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
