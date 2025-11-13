import customtkinter 
from sequencer import StepButton, SequencerFrame
from sound_select import SoundSelectFrame, SoundSelectButton
from faders import VolumeFaderFrame, VolumeFader

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Init root window -------------------------------------------
        self.title("PY-808")
        self.geometry("1220x650")

        # Init frames
        self.sequencer = SequencerFrame(self)
        self.sound_select_buttons = SoundSelectFrame(self)
        self.fader_frame = VolumeFaderFrame(self)

        # position frames
        self.sequencer.grid(row=3, column=0)
        self.sound_select_buttons.grid(row=2, column=0)
        self.fader_frame.grid(row=1, column=0)

        self.grid_columnconfigure(0, weight=1)

        


def main():
    root = Root()
    root.sequencer.create()
    root.sound_select_buttons.create()
    root.fader_frame.create()
    root.mainloop()

main()
