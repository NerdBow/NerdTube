import customtkinter as ctk


class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(master=master)

        self.path_button = ctk.CTkButton()
        self.path_button.grid()

        self.mp3_switch = ctk.CTkSwitch()
        self.mp3_switch.grid()

        self.download_button = ctk.CTkButton()
        self.download_button.grid()
