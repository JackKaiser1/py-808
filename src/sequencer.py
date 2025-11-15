import customtkinter 
from constants import STEP_HEIGHT, STEP_WIDTH, GREY_1, GREY_2, STEP_PAD_X, STEP_PAD_Y, ORANGE_1, ORANGE_2
from custom_frame import CustomFrame
from sound_mixer import drum

class StepButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            height=STEP_HEIGHT, 
            width=STEP_WIDTH, 
            hover=None,
            command=lambda: self.populate_step(self, drum.current_drum),
            *args, 
            **kwargs) 
        

    def populate_step(self, step, current_drum):
        beat = int(step._text)
        beat_list = current_drum.beat_list
        back_beat = [5,6,7,8,13,14,15,16]
        step_color = step._fg_color

        if step_color == GREY_1:
            beat_list.add(beat)
            step.configure(fg_color=ORANGE_1)
        elif step_color == GREY_2:
            beat_list.add(beat)
            step.configure(fg_color=ORANGE_2)

        elif beat in back_beat and step_color == ORANGE_2:
            beat_list.remove(beat)
            step.configure(fg_color=GREY_2)
        else:
            beat_list.remove(beat)
            step.configure(fg_color=GREY_1)

        print(beat_list)
        
    

        

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


    def display_pattern(self):
        step_list = self.step_list

        for step in step_list:
            step_num = int(step._text)
            beat_list = drum.current_drum.beat_list

            if step_num in beat_list:
                if step._fg_color == GREY_1:
                    step.configure(fg_color=ORANGE_1)
                elif step._fg_color == GREY_2:
                    step.configure(fg_color=ORANGE_2)

            elif step._fg_color == ORANGE_1:
                step.configure(fg_color=GREY_1)
            elif step._fg_color == ORANGE_2:
                step.configure(fg_color=GREY_2)