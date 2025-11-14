import customtkinter 
from sequencer import StepButton, SequencerFrame
from sound_select import SoundSelectFrame, SoundSelectButton
from faders import VolumeFaderFrame, VolumeFader
from control_buttons_frame import ControlButtonsFrame


class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()     

        # Init root window -------------------------------------------
        self.title("PY-808")
        self.geometry("1220x650")

        # Init frames
        self.sequencer = SequencerFrame(self)
        self.sound_select_buttons = SoundSelectFrame(self)
        self.faders = VolumeFaderFrame(self)
        self.control_buttons = ControlButtonsFrame(self)

        # Position frames
        self.sequencer.grid(row=3, column=0, pady=10)
        self.sound_select_buttons.grid(row=2, column=0, pady=10)
        self.faders.grid(row=1, column=0, pady=(20, 10))
        self.control_buttons.grid(row=0, column=0, pady=(60, 10))

        # Center widgets in column 0
        self.grid_columnconfigure(0, weight=1)



        


def main():
    root = Root()
    root.sequencer.create()
    root.sound_select_buttons.create()
    root.faders.create()
    root.mainloop()

main()
