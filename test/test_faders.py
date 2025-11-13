import sys
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
import customtkinter 
from constants import *
from faders import VolumeFaderFrame

root = customtkinter.CTk()
frame = VolumeFaderFrame(root)
frame.grid(row=0, column=0)
frame.create()

class TestVolumeFaderFrame(unittest.TestCase):
    # Tests for create() ----------------------------------------
    def test_create_height(self):
        fader_orientation = frame.fader_list[4]._orientation
        self.assertEqual("vertical", fader_orientation)


    # Tests for position() --------------------------------------
    def test_position_column(self):
        fader_column = frame.fader_list[5].grid_info()["column"]
        self.assertEqual(5, fader_column)

    def test_position_row(self):
        fader_row = frame.fader_list[11].grid_info()["row"]
        self.assertEqual(0, fader_row)

    def test_position_padx(self):
        fader_padx = frame.fader_list[2].grid_info()["padx"]
        self.assertEqual(FADER_PAD_X, fader_padx)

    def test_position_pady(self):
        fader_pady = frame.fader_list[7].grid_info()["pady"]
        self.assertEqual(FADER_PAD_Y, fader_pady)    