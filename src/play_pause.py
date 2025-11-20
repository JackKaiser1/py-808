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
        
    def play(self):
        # i = 0
        # count = 1
        # if count > i:
        loop()  

        # time.sleep(0.1)
        # i += 1
        # count += 1

        # if count == 16:
        #     i = 0
        #     count = 1
        PlayButton.after(self, 110, self.play)

    def start(self):
        loop()
        while True:
            # self.play()
            PlayButton.after(self, 110, loop())

        
     

        