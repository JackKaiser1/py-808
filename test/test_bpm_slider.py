import sys
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
import customtkinter 
from constants import *
from bpm_slider import BPMSliderFrame
from sequencer import StepButton, SequencerFrame
from sound_select import SoundSelectFrame, SoundSelectButton
from faders import VolumeFaderFrame, VolumeFader
from control_buttons_frame import ControlButtonsFrame

class TestRoot(customtkinter.CTk):
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

root = TestRoot()
root.sequencer.create()
root.sound_select_buttons.create(root)
root.faders.create()


class TestBPMSliderFrame(unittest.TestCase):
    def test_bpm_slider_label(self):
        self.assertEqual(130, root.control_buttons.bpm.bpm_slider.get())

    def test_set_BPM_1(self):
        interval = root.control_buttons.bpm.set_bpm(70, root)
        self.assertEqual(0.214, interval)
        
    def test_set_BPM_2(self):
        interval = root.control_buttons.bpm.set_bpm(140, root)
        self.assertEqual(0.107, interval)