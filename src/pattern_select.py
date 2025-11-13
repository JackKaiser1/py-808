import customtkinter
from constants import PATTERN_SELECT_HEIGHT, PATTERN_SELECT_WIDTH

class PatternSelect(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=PATTERN_SELECT_HEIGHT,
            width=PATTERN_SELECT_WIDTH,
            *args, 
            **kwargs)
        

