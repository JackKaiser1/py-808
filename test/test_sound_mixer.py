import sys 
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
import customtkinter
from sequencer import StepButton, SequencerFrame
from sound_select import SoundSelectFrame, SoundSelectButton
from faders import VolumeFaderFrame, VolumeFader
from control_buttons_frame import ControlButtonsFrame
from sound_mixer import *
from sound_class import drum, counter


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

class TestDrumRack(unittest.TestCase):
    def test_loop_counter_1(self):
        counter.count = 0

        drum_rack.loop()
        self.assertEqual(1, counter.count)

    def test_loop_counter_2(self):
        counter.count = 0

        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        self.assertEqual(5, counter.count)

    def test_loop_counter_3(self):
        counter.count = 0

        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        self.assertEqual(10, counter.count)

    def test_loop_counter_4(self):
        counter.count = 0

        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        self.assertEqual(1, counter.count)



    def test_loop_beat_list_1(self):
        counter.count = 0
        kick_button = root.sound_select_buttons.sound_buttons[0]
        beat_list = drum.current_drum.beat_list
        select_drum = root.sound_select_buttons.select_drum

        select_drum(kick_button, root)
        beat_list.add(1)

        self.assertEqual([{1}], drum_rack.loop())
        beat_list.clear()

    def test_loop_beat_list_2(self):
        counter.count = 0
        kick_button = root.sound_select_buttons.sound_buttons[0]
        beat_list = drum.current_drum.beat_list
        select_drum = root.sound_select_buttons.select_drum

        select_drum(kick_button, root)
        beat_list.add(1)
        beat_list.add(10)

        self.assertEqual([{1, 10}], drum_rack.loop())
        beat_list.clear()

    def test_loop_beat_list_3(self):
        counter.count = 0
        snare_button = root.sound_select_buttons.sound_buttons[1]
        beat_list = drum.current_drum.beat_list
        select_drum = root.sound_select_buttons.select_drum

        select_drum(snare_button, root)
        beat_list.add(5)
        beat_list.add(8)

        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()
        drum_rack.loop()

        self.assertEqual([{5, 8}], drum_rack.loop())
        beat_list.clear()