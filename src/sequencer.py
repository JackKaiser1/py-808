import customtkinter 
from constants import STEP_HEIGHT, STEP_WIDTH, GREY_1, GREY_2, STEP_PAD_X, STEP_PAD_Y

class StepButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=STEP_HEIGHT, 
            width=STEP_WIDTH, 
            hover=None,
            *args, 
            **kwargs) 
        
    

        

class SequencerFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.step_list = []

    def init_steps(self):
        for i in range(1, 17):
            if i in [1, 2, 3, 4, 9, 10, 11, 12]:
                self.step_list.append(StepButton(self, text=f"{i}", fg_color=GREY_1))
            else:
                self.step_list.append(StepButton(self, text=f"{i}", fg_color=GREY_2))
        
    def position_steps(self):
        i = 0
        for step in self.step_list:
            step.grid(row=0, column=i, padx=STEP_PAD_X, pady=STEP_PAD_Y) 
            i += 1 











        # Init StepButton objects / Position StepButton objects
        # self.step_1 = StepButton(self, text="1", fg_color=GREY_1).grid(row=0, column=0, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_2 = StepButton(self, text="2", fg_color=GREY_1).grid(row=0, column=1, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_3 = StepButton(self, text="3", fg_color=GREY_1).grid(row=0, column=2, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_4 = StepButton(self, text="4", fg_color=GREY_1).grid(row=0, column=3, padx=STEP_PAD_X, pady=STEP_PAD_Y)

        # self.step_5 = StepButton(self, text="5", fg_color=GREY_2).grid(row=0, column=4, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_6 = StepButton(self, text="6", fg_color=GREY_2).grid(row=0, column=5, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_7 = StepButton(self, text="7", fg_color=GREY_2).grid(row=0, column=6, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_8 = StepButton(self, text="8", fg_color=GREY_2).grid(row=0, column=7, padx=STEP_PAD_X, pady=STEP_PAD_Y)

        # self.step_9 = StepButton(self, text="9", fg_color=GREY_1).grid(row=0, column=8, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_10 = StepButton(self, text="10", fg_color=GREY_1).grid(row=0, column=9, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_11 = StepButton(self, text="11", fg_color=GREY_1).grid(row=0, column=10, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_12 = StepButton(self, text="12", fg_color=GREY_1).grid(row=0, column=11, padx=STEP_PAD_X, pady=STEP_PAD_Y)

        # self.step_13 = StepButton(self, text="13", fg_color=GREY_2).grid(row=0, column=12, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_14 = StepButton(self, text="14", fg_color=GREY_2).grid(row=0, column=13, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_15 = StepButton(self, text="15", fg_color=GREY_2).grid(row=0, column=14, padx=STEP_PAD_X, pady=STEP_PAD_Y)
        # self.step_16 = StepButton(self, text="16", fg_color=GREY_2).grid(row=0, column=15, padx=STEP_PAD_X, pady=STEP_PAD_Y)


        
      
        

























