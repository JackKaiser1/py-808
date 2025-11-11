import customtkinter

class BPMSlider(customtkinter.CTkSlider):
    def __init__(self):
        super().__init__()
        

class BPMSliderFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        