import customtkinter as ctk


class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(master=master)

        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.path_button = ctk.CTkButton(master=self, text="Output Path")
        self.path_button.grid(row=0, column=0, padx=20, pady=20)

        self.mp3_switch = ctk.CTkSwitch(master=self, text="MP3")
        self.mp3_switch.grid(row=1, column=0, padx=20, pady=20)

        self.download_button = ctk.CTkButton(master=self, text="Download")
        self.download_button.grid(row=2, column=0, padx=20, pady=20)
