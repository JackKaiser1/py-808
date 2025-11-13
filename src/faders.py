import customtkinter 
from constants import FADER_HEIGHT, FADER_PAD_X, FADER_PAD_Y
from custom_frame import CustomFrame

class VolumeFader(customtkinter.CTkSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            from_=0,
            to=100,
            orientation="vertical",
            height=FADER_HEIGHT,
            *args, 
            **kwargs)
        

class VolumeFaderFrame(CustomFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.fader_list = []

    def create(self):
        for _ in range(0, 16):
            self.fader_list.append(VolumeFader(self))
        self.position()

    def position(self):
        i = 0
        for fader in self.fader_list:
            fader.grid(row=0, column=i, padx=FADER_PAD_X, pady=FADER_PAD_Y)
            i += 1