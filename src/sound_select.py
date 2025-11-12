import customtkinter 
from constants import SOUND_BUTTON_HEIGHT, SOUND_BUTTON_WIDTH, SOUND_BUTTON_PAD_x, SOUND_BUTTON_PAD_Y, GREY_1
from drum_name_dict import drum_name_dict

class SoundSelectButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=SOUND_BUTTON_HEIGHT,
            width=SOUND_BUTTON_WIDTH,
            hover=None,
            fg_color=GREY_1,
            font=("Arial", 9),
            *args, 
            **kwargs)
    
        

class SoundSelectFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.sound_button_list = []

    def init_sound_buttons(self):
        drum_names = drum_name_dict.keys()
        for drum_name in drum_names:
            self.sound_button_list.append(SoundSelectButton(self, text=drum_name))

    def position_sound_buttons(self):
        i = 0
        for sound_button in self.sound_button_list:
            sound_button.grid(row=0, column=i, padx=SOUND_BUTTON_PAD_x, pady=SOUND_BUTTON_PAD_Y)
            i += 1




    