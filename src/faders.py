import customtkinter 
from constants import FADER_HEIGHT, FADER_PAD_X, FADER_PAD_Y, ORANGE_2, ORANGE_1
from custom_frame import CustomFrame
from drum_name_dict import drum_name_dict

class VolumeFader(customtkinter.CTkSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            from_=0,
            to=1,
            orientation="vertical",
            height=FADER_HEIGHT,
            button_color=ORANGE_1,
            hover=None,
            *args, 
            **kwargs)
        

class VolumeFaderFrame(CustomFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.fader_list = []

    def create(self):
        for _ in range(0, 16):
            self.fader_list.append(VolumeFader(self))

        self.init_command()
        self.position()

    def position(self):
        i = 0
        for fader in self.fader_list:
            fader.grid(row=0, column=i, padx=FADER_PAD_X, pady=FADER_PAD_Y)
            i += 1

    def init_command(self):
        faders = self.fader_list 
        drums = list(drum_name_dict.values())
        i = 0

        for fader in faders:
            self.set_command(fader, drums[i])
            i += 1


    def set_command(self, fader, drum_obj):
        fader.configure(command=lambda vol: self.set_volume(vol, drum_obj))

    def set_volume(self, vol, drum_obj):
        drum_obj.volume = vol 
        return drum_obj.volume
