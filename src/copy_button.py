import customtkinter
from constants import PATTERN_COPY_HEIGHT, PATTERN_COPY_WIDTH, GREY_1

class CopyButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=PATTERN_COPY_HEIGHT,
            width=PATTERN_COPY_WIDTH,
            text="COPY",
            fg_color=GREY_1,
            *args, 
            **kwargs)

