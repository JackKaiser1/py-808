import customtkinter  
from play_pause import PlayButton
from bpm_slider import BPMSliderFrame
from pattern_select import PatternSelect
from copy_button import CopyButton

class ControlButtonsFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Init objects buttons
        self.play_button = PlayButton(self)
        self.bpm = BPMSliderFrame(self)
        self.pattern_button = PatternSelect(self)
        self.copy_button = CopyButton(self)

        # Position button objects
        self.play_button.grid(row=0, column=0, padx=(10, 550), pady=10)
        self.bpm.grid(row=0, column=1, padx=10, pady=10)
        self.pattern_button.grid(row=0, column=2, padx=10, pady=10)
        self.copy_button.grid(row=0, column=3, padx=10, pady=10)