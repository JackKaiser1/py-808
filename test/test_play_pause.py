import sys 
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
import customtkinter
from sequencer import StepButton, SequencerFrame
from sound_select import SoundSelectFrame, SoundSelectButton
from faders import VolumeFaderFrame, VolumeFader
from control_buttons_frame import ControlButtonsFrame
from sound_mixer import *
from sound_class import drum


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
drum.current_drum = drum_rack.kick
root.sequencer.create()
root.sound_select_buttons.create(root)
root.faders.create()


class TestPlayButton(unittest.TestCase):
    def test_play_button_hide_play(self):
        root.control_buttons.play(root)

        self.assertEqual({}, root.control_buttons.play_button.grid_info())

    def test_play_button_draw_pause_1(self):
        root.control_buttons.play(root)

        self.assertEqual((10, 650), root.control_buttons.pause_button.grid_info()["padx"])

    def test_play_button_draw_pause_2(self):
        root.control_buttons.play(root)

        self.assertEqual(10, root.control_buttons.pause_button.grid_info()["pady"])


class TestPauseButton(unittest.TestCase):
    def test_pause_button_1(self):
        root.control_buttons.pause()

        self.assertEqual(True, root.control_buttons.pause_track)
        root.control_buttons.play(root)

    def test_pause_button_hide_pause(self):
        root.control_buttons.pause()

        self.assertEqual({}, root.control_buttons.pause_button.grid_info())
        root.control_buttons.play(root)

    def test_pause_button_draw_play_1(self):
        root.control_buttons.pause()

        self.assertEqual((10, 650), root.control_buttons.play_button.grid_info()["padx"])
        root.control_buttons.play(root)

    def test_pause_button_draw_play_2(self):
        root.control_buttons.pause()

        self.assertEqual(10, root.control_buttons.play_button.grid_info()["pady"])
        root.control_buttons.play(root)

    
    

