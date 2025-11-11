import customtkinter 
from constants import STEP_HEIGHT, STEP_WIDTH, GREY_1, GREY_2

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

        # Init StepButton objects
        self.step_1 = StepButton(self, text="1", fg_color=GREY_1)
        self.step_2 = StepButton(self, text="2", fg_color=GREY_1)
        self.step_3 = StepButton(self, text="3", fg_color=GREY_1)
        self.step_4 = StepButton(self, text="4", fg_color=GREY_1)

        # Position steps
        self.step_1.grid(row=0, column=0)
        self.step_2.grid(row=0, column=1)
        self.step_3.grid(row=0, column=2)
        self.step_4.grid(row=0, column=3)

       
      
        






















 # for i in range(1, 17):
        #     if i in [1, 2, 3, 4, 9, 10, 11, 12]:
        #         step = StepButton(self, 
        #                             text=f"{i}", 
        #                             height=STEP_WIDTH, 
        #                             width=STEP_HEIGHT,
        #                             hover=None,
        #                             fg_color=GREY_1)
        #         self.step_list.append(step)
        #     else:
        #         step = StepButton(self, 
        #                             text=f"{i}", 
        #                             height=STEP_WIDTH, 
        #                             width=STEP_HEIGHT,
        #                             hover=None,
        #                             fg_color=GREY_2)
        #         self.step_list.append(step)


