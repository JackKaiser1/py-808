import customtkinter 

class VolumeFader(customtkinter.CTkSlider):
    def __init__(self):
        super().__init__()
        

class VolumeFaderFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        