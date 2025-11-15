import customtkinter 
from constants import SOUND_BUTTON_HEIGHT, SOUND_BUTTON_WIDTH, SOUND_BUTTON_PAD_X, SOUND_BUTTON_PAD_Y, GREY_1
from drum_name_dict import drum_name_dict
from custom_frame import CustomFrame
from sound_mixer import drum
from drum_name_dict import drum_name_dict
from constants import *

class SoundSelectButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=SOUND_BUTTON_HEIGHT,
            width=SOUND_BUTTON_WIDTH,
            hover=None,
            font=("Arial", 9),
            *args, 
            **kwargs)
        
    

class SoundSelectFrame(CustomFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.sound_buttons = []


    def create(self):
        drum_names = drum_name_dict.keys()
        sound_buttons = self.sound_buttons
        for drum_name in drum_names:
            if drum_name == "KICK":
                sound_buttons.append(SoundSelectButton(self, text=drum_name, fg_color=ORANGE_1))
            else:
                sound_buttons.append(SoundSelectButton(self, text=drum_name, fg_color=GREY_1))

        self.init_command()
        self.position()


    def init_command(self):
        sound_buttons = self.sound_buttons 
        for sound_button in sound_buttons:
            self.set_command(sound_button)


    def set_command(self, sound_button):
        sound_button.configure(command=lambda: self.select_drum(sound_button))


    def position(self):
        i = 0
        for sound_button in self.sound_buttons:
            sound_button.grid(row=0, column=i, padx=SOUND_BUTTON_PAD_X, pady=SOUND_BUTTON_PAD_Y)
            i += 1
    

    def select_drum(self, sound_button):
        selected_drum_name = sound_button._text
        print(selected_drum_name)
        new_drum_sound = drum_name_dict[selected_drum_name]

        drum.current_drum = new_drum_sound
        self.activate_button(sound_button)


    def activate_button(self, selected_button):
        sound_buttons = self.sound_buttons
        for inactive_button in sound_buttons:
            if inactive_button._fg_color == ORANGE_1:
                inactive_button.configure(fg_color=GREY_1)

        selected_button.configure(fg_color=ORANGE_1)







    