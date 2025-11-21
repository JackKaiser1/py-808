import sys
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src/assets")


import unittest
import customtkinter 
from sequencer import SequencerFrame, StepButton
from sound_select import SoundSelectFrame
from constants import *
from src.assets import *
from sound_mixer import drum

# root = customtkinter.CTk()
# frame = SequencerFrame(root)
# frame.grid(row=0, column=0)
# frame.create()

class TestRoot(customtkinter.CTk):
    def __init__(self):
        super().__init__()     

        # Init root window -------------------------------------------
        self.title("PY-808")
        self.geometry("1220x650")

        # Init frames
        self.sequencer = SequencerFrame(self)
        self.sound_select_buttons = SoundSelectFrame(self)

        # Position frames
        self.sequencer.grid(row=3, column=0, pady=10)
        self.sound_select_buttons.grid(row=2, column=0, pady=10)

        # Center widgets in column 0
        self.grid_columnconfigure(0, weight=1)

root = TestRoot()
root.withdraw()

root.sequencer.create()
root.sound_select_buttons.create(root)

class TestSequencerFrame(unittest.TestCase):
    
    # Tests for create() ----------------------------------------
    def test_create_text(self):
        self.assertEqual("4", root.sequencer.step_list[3]._text)

    def test_create_color_grey1(self):
        self.assertEqual(GREY_1, root.sequencer.step_list[1]._fg_color)

    def test_create_color_grey2(self):
        self.assertEqual(GREY_2, root.sequencer.step_list[4]._fg_color)


    # Tests for position() ----------------------------------------
    def test_position_column(self):
        grid_info = root.sequencer.step_list[5].grid_info()
        self.assertEqual(5, grid_info["column"])

    def test_position_row(self):
        grid_info = root.sequencer.step_list[8].grid_info()
        self.assertEqual(0, grid_info["row"])

    def test_position_padx(self):
        grid_info = root.sequencer.step_list[5].grid_info()
        self.assertEqual(STEP_PAD_X, grid_info["padx"])

    def test_position_pady(self):
        grid_info = root.sequencer.step_list[9].grid_info()
        self.assertEqual(STEP_PAD_Y, grid_info["pady"])

    # Test display_pattern
    def test_display_pattern_snare(self):
        snare_button = root.sound_select_buttons.sound_buttons[1]
        kick_button = root.sound_select_buttons.sound_buttons[0]
        root.sound_select_buttons.select_drum(snare_button, root)

        beat_list = drum.current_drum.beat_list
        beat_list.add(3)
        beat_list.add(7)

        root.sound_select_buttons.select_drum(kick_button, root)

        beat_list = drum.current_drum.beat_list
        beat_list.add(4)
        beat_list.add(10)

        root.sound_select_buttons.select_drum(snare_button, root)

        self.assertEqual(ORANGE_1, root.sequencer.step_list[2]._fg_color)
        self.assertEqual(ORANGE_2, root.sequencer.step_list[6]._fg_color)

        drum.current_drum.beat_list.clear()
        root.sound_select_buttons.select_drum(kick_button, root)
        beat_list = drum.current_drum.beat_list
        drum.current_drum.beat_list.clear()


    def test_display_pattern_kick(self):
        snare_button = root.sound_select_buttons.sound_buttons[1]
        kick_button = root.sound_select_buttons.sound_buttons[0]
        root.sound_select_buttons.select_drum(snare_button, root)

        beat_list = drum.current_drum.beat_list
        beat_list.add(3)
        beat_list.add(7)

        root.sound_select_buttons.select_drum(kick_button, root)

        beat_list = drum.current_drum.beat_list
        beat_list.add(4)
        beat_list.add(10)

        root.sound_select_buttons.select_drum(snare_button, root)
        root.sound_select_buttons.select_drum(kick_button, root)

        self.assertEqual(ORANGE_1, root.sequencer.step_list[3]._fg_color)
        self.assertEqual(ORANGE_1, root.sequencer.step_list[9]._fg_color)

        drum.current_drum.beat_list.clear()
        root.sound_select_buttons.select_drum(kick_button, root)
        beat_list = drum.current_drum.beat_list
        drum.current_drum.beat_list.clear()





class TestStepButton(unittest.TestCase):
    def test_populate_steps_orange_1(self):
        step_2 = root.sequencer.step_list[1]
        step_2.populate_step(step_2, drum.current_drum)
        self.assertEqual(ORANGE_1, step_2._fg_color)
        drum.current_drum.beat_list.clear()

    def test_populate_steps_orange_2(self):
        step_6 = root.sequencer.step_list[5]
        step_6.populate_step(step_6, drum.current_drum)
        self.assertEqual(ORANGE_2, step_6._fg_color)
        drum.current_drum.beat_list.clear()

    def test_populate_steps_grey_1(self):
        step_2 = root.sequencer.step_list[1]
        step_2.populate_step(step_2, drum.current_drum)
        step_2.populate_step(step_2, drum.current_drum)
        self.assertEqual(GREY_1, step_2._fg_color)
        drum.current_drum.beat_list.clear()

    def test_populate_steps_grey_2(self):
        step_6 = root.sequencer.step_list[5]
        step_6.populate_step(step_6, drum.current_drum)
        step_6.populate_step(step_6, drum.current_drum)
        self.assertEqual(GREY_2, step_6._fg_color)
        drum.current_drum.beat_list.clear()




