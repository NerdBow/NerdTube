import customtkinter
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
        self.columnconfigure((0, 1, 2, 3), weight=1)
        self.rowconfigure((0), weight=1)

        self.search_frame = SearchFrame(self)
        self.search_frame.grid(
            row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nwe"
        )
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
