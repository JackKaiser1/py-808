import sys
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src/assets")


import unittest
import customtkinter 
from sequencer import SequencerFrame, StepButton
from constants import *
from src.assets import *
from sound_mixer import drum

root = customtkinter.CTk()
frame = SequencerFrame(root)
frame.grid(row=0, column=0)
frame.create()

class TestSequencerFrame(unittest.TestCase):
    
    # Tests for create() ----------------------------------------
    def test_create_text(self):
        self.assertEqual("4", frame.step_list[3]._text)

    def test_create_color_grey1(self):
        self.assertEqual(GREY_1, frame.step_list[1]._fg_color)

    def test_create_color_grey2(self):
        self.assertEqual(GREY_2, frame.step_list[4]._fg_color)


    # Tests for position() ----------------------------------------
    def test_position_column(self):
        grid_info = frame.step_list[5].grid_info()
        self.assertEqual(5, grid_info["column"])

    def test_position_row(self):
        grid_info = frame.step_list[8].grid_info()
        self.assertEqual(0, grid_info["row"])

    def test_position_padx(self):
        grid_info = frame.step_list[5].grid_info()
        self.assertEqual(STEP_PAD_X, grid_info["padx"])

    def test_position_pady(self):
        grid_info = frame.step_list[9].grid_info()
        self.assertEqual(STEP_PAD_Y, grid_info["pady"])


class TestStepButton(unittest.TestCase):
    def test_populate_steps_orange_1(self):
        step_2 = frame.step_list[1]
        step_2.populate_step(step_2, drum.current_drum)
        self.assertEqual(ORANGE_1, step_2._fg_color)
        drum.current_drum.beat_list.clear()

    def test_populate_steps_orange_2(self):
        step_6 = frame.step_list[5]
        step_6.populate_step(step_6, drum.current_drum)
        self.assertEqual(ORANGE_2, step_6._fg_color)
        drum.current_drum.beat_list.clear()

    def test_populate_steps_grey_1(self):
        step_2 = frame.step_list[1]
        step_2.populate_step(step_2, drum.current_drum)
        step_2.populate_step(step_2, drum.current_drum)
        self.assertEqual(GREY_1, step_2._fg_color)
        drum.current_drum.beat_list.clear()

    def test_populate_steps_grey_2(self):
        step_6 = frame.step_list[5]
        step_6.populate_step(step_6, drum.current_drum)
        step_6.populate_step(step_6, drum.current_drum)
        self.assertEqual(GREY_2, step_6._fg_color)
        drum.current_drum.beat_list.clear()




