import customtkinter
from constants import BPM_LABEL_HEIGHT, BPM_LABEL_WIDTH, GREY_1

class BPMSlider(customtkinter.CTkSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            orientation="horizontal",
            from_=10,
            to=250,
            *args, 
            **kwargs)
        
class BPMLabel(customtkinter.CTkLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=BPM_LABEL_HEIGHT,
            width=BPM_LABEL_WIDTH,
            fg_color=None,
            font=("Arial", 22),
            *args, 
            **kwargs)
        
    def get_value(self, bpm_slider_value):
        self.configure(text=bpm_slider_value)

class BPMSliderFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Init slider and label 
        self.bpm_slider = BPMSlider(self)
        self.bpm_label = BPMLabel(self, text=self.bpm_slider.get())

        # Position slider and label
        self.bpm_slider.grid(row=1, column=0, padx=5, pady=5)
        self.bpm_label.grid(row=0, column=0, padx=5, pady=5)