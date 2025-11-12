import customtkinter 
from constants import STEP_HEIGHT, STEP_WIDTH, GREY_1, GREY_2, STEP_PAD_X, STEP_PAD_Y
from custom_frame import CustomFrame

class StepButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=STEP_HEIGHT, 
            width=STEP_WIDTH, 
            hover=None,
            *args, 
            **kwargs) 
        
    

        

class SequencerFrame(CustomFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.step_list = []

    def create(self):
        for i in range(1, 17):
            if i in [1, 2, 3, 4, 9, 10, 11, 12]:
                self.step_list.append(StepButton(self, text=f"{i}", fg_color=GREY_1))
            else:
                self.step_list.append(StepButton(self, text=f"{i}", fg_color=GREY_2))
        self.position()
        
    def position(self):
        i = 0
        for step in self.step_list:
            step.grid(row=0, column=i, padx=STEP_PAD_X, pady=STEP_PAD_Y) 
            i += 1 
