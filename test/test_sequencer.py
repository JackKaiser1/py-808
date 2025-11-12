import sys
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
import customtkinter 
import src.sequencer
import src.constants
from src.sequencer import SequencerFrame, StepButton
from src.constants import *

root = customtkinter.CTk()

class TestSequencerFrame(unittest.TestCase):
    # Tests for create
    def test_create_text(self):
        frame = SequencerFrame(root)
        frame.grid(row=0, column=0)
        frame.create()
        self.assertEqual("4", frame.step_list[3]._text)

    def test_create_color_grey1(self):
        frame = SequencerFrame(root)
        frame.grid(row=0, column=0)
        frame.create()
        self.assertEqual(GREY_1, frame.step_list[1]._fg_color)

    def test_create_color_grey2(self):
        frame = SequencerFrame(root)
        frame.grid(row=0, column=0)
        frame.create()
        # frame.position_steps()
        self.assertEqual(GREY_2, frame.step_list[4]._fg_color)

    # Tests for position


