import customtkinter
from constants import BPM_LABEL_HEIGHT, BPM_LABEL_WIDTH, GREY_1, ORANGE_1, GREY_2, BPM_COLOR

class BPMSlider(customtkinter.CTkSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            orientation="horizontal",
            from_=10,
            to=250,
            button_color=ORANGE_1,
            hover=None,
            *args, 
            **kwargs)
                
        
        
class BPMLabel(customtkinter.CTkLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=BPM_LABEL_HEIGHT,
            width=BPM_LABEL_WIDTH,
            fg_color=None,
            font=("Roboto", 22),
            text_color=BPM_COLOR,
            *args, 
            **kwargs)
        
    def get_value(self, bpm_slider_value):
        self.configure(text=int(bpm_slider_value))
        return bpm_slider_value


class BPMSliderFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Init slider and label 
        self.bpm_label = BPMLabel(self, text="130")
        self.bpm_slider = BPMSlider(self, command=lambda bpm: [self.set_bpm(bpm, parent), self.bpm_label.get_value(bpm)])

        # Position slider and label
        self.bpm_slider.grid(row=1, column=0, padx=5, pady=5)
        self.bpm_label.grid(row=0, column=0, padx=5, pady=(15, 5))


    def set_bpm(self, bpm, parent):
        # Calculate the length of one 16th note
        interval = ((60_000 // int(bpm)) // 4) / 1000
        parent.interval = interval
        return interval