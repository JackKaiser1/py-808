import customtkinter
from constants import PLAY_PAUSE_HEIGHT, PLAY_PAUSE_WIDTH, GREY_1

class PlayButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=PLAY_PAUSE_HEIGHT,
            width=PLAY_PAUSE_WIDTH,
            text="PLAY",
            fg_color=GREY_1,
            *args, 
            **kwargs)
        
     

        