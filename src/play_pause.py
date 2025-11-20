import customtkinter
from constants import PLAY_PAUSE_HEIGHT, PLAY_PAUSE_WIDTH, GREY_1
from sound_mixer import *
import time

class PlayButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=PLAY_PAUSE_HEIGHT,
            width=PLAY_PAUSE_WIDTH,
            text="PLAY",
            command=self.play,
            fg_color=GREY_1,
            *args, 
            **kwargs)
        
        self.playing = False
        self.played = 0
        
    def play(self):
        loop()  
        PlayButton.after(self, 110, self.play)

    
        
        
     

        