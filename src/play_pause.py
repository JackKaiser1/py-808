import customtkinter
from constants import PLAY_PAUSE_HEIGHT, PLAY_PAUSE_WIDTH, GREY_1, ORANGE_1, GREY_2, ORANGE_2
from sound_mixer import *
import time

class PlayButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=PLAY_PAUSE_HEIGHT,
            width=PLAY_PAUSE_WIDTH,
            text="PLAY",
            font=("Roboto", 12),
            fg_color=GREY_1,
            hover=GREY_2,
            *args, 
            **kwargs)

class PauseButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=PLAY_PAUSE_HEIGHT,
            width=PLAY_PAUSE_WIDTH,
            text="PAUSE",
            font=("Roboto", 12),
            fg_color=ORANGE_1,
            hover=ORANGE_2,
            *args, 
            **kwargs)

    
        
        
     

        