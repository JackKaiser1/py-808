import sys
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
import customtkinter 
from sequencer import SequencerFrame, StepButton
from constants import *

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
