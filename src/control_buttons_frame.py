import customtkinter  
from play_pause import PlayButton, PauseButton
from bpm_slider import BPMSliderFrame
from pattern_select import PatternSelect
from copy_button import CopyButton
from sound_mixer import drum_rack
from sound_class import counter

class ControlButtonsFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Init objects buttons
        self.play_button = PlayButton(self, command=self.play)
        self.pause_button = PauseButton(self, command=self.pause)
        self.bpm = BPMSliderFrame(self)

        # Position button objects
        self.play_button.grid(row=0, column=0, padx=(10, 550), pady=10)
        self.bpm.grid(row=0, column=1, padx=10, pady=10)

        self.pause_track = False



    def play(self):
        if self.pause_track == True:
            self.pause_track = False
            return 
        
        self.play_button.grid_forget()
        self.pause_button.grid(row=0, column=0, padx=(10, 550), pady=10)

        drum_rack.loop()  
        PlayButton.after(self, 110, self.play)

    def pause(self):
        self.pause_track = True
        self.pause_button.grid_forget()
        self.play_button.grid(row=0, column=0, padx=(10, 550), pady=10)
        counter.count = 0

