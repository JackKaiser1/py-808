import customtkinter  
from play_pause import PlayButton, PauseButton
from bpm_slider import BPMSliderFrame
from pattern_select import PatternSelect
from copy_button import CopyButton
from sound_mixer import drum_rack
from sound_class import counter
import time

class ControlButtonsFrame(customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, 
                         fg_color="transparent",
                         *args, 
                         **kwargs)

        # Init objects buttons
        self.play_button = PlayButton(self, command=lambda: self.play(parent))
        self.pause_button = PauseButton(self, command=self.pause)
        self.bpm = BPMSliderFrame(self)

        # Position button objects
        self.play_button.grid(row=0, column=0, padx=(10, 650), pady=10)
        self.bpm.grid(row=0, column=1, padx=10, pady=10)

        self.pause_track = False

        self.next_beat = time.monotonic()
        self.interval = 0.115 



    def play(self, parent):
        if self.pause_track == True:
            self.pause_track = False
            parent.sequencer.stop_display_tempo()
            return 
        
        self.play_button.grid_forget()
        self.pause_button.grid(row=0, column=0, padx=(10, 650), pady=10)

        current = time.monotonic()
        
        if current >= self.next_beat:
            drum_rack.loop()  
            parent.sequencer.display_tempo()

            self.next_beat = time.monotonic() + self.interval

            if parent.sequencer.switch_pattern == True:
                parent.sequencer.display_pattern()
                parent.sequencer.switch_pattern = False

        PlayButton.after(self, 1, self.play, parent)
        

    def pause(self):
        self.pause_track = True
        self.pause_button.grid_forget()
        self.play_button.grid(row=0, column=0, padx=(10, 650), pady=10)
        counter.count = 0


