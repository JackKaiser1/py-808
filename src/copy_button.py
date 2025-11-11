import customtkinter

class CopyButton(customtkinter.CTkButton):
    def __init__(self):
        super().__init__()

class CopyButtonFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)