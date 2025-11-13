import customtkinter  
from play_pause import PlayButton
from bpm_slider import BPMSliderFrame

class ControlButtonsFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Init objects buttons
        self.play_button = PlayButton(self)
        self.bpm = BPMSliderFrame(self)

        # Position button objects
        self.play_button.grid(row=0, column=0, padx=10, pady=10)
        self.bpm.grid(row=0, column=1, padx=10, pady=10)
