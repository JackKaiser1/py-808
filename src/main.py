import customtkinter 
from sequencer import StepButton, SequencerFrame

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Init root window -------------------------------------------
        self.title("PY-808")
        self.geometry("1220x650")

        # Init frames
        self.sequencer = SequencerFrame(self)

        # position frames
        self.sequencer.grid(row=3, column=0)

        self.grid_columnconfigure(0, weight=1)

        


def main():
    root = Root()
    root.sequencer.init_steps()
    root.sequencer.position_steps()
    root.mainloop()

main()
