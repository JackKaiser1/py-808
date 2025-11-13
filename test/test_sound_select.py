import sys 
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
import customtkinter
from sound_select import SoundSelectFrame
from constants import *

root = customtkinter.CTk()
frame = SoundSelectFrame(root)
frame.grid(row=0, column=0)
frame.create()

class TestSoundSelectFrame(unittest.TestCase):
    # Tests for create() ----------------------------------------
    def test_create_drum_name_1(self):
        button_4_drum_name = frame.sound_button_list[3]._text
        self.assertEqual("HHAT", button_4_drum_name)

    def test_create_drum_name_2(self):
        button_8_drum_name = frame.sound_button_list[7]._text
        self.assertEqual("OHAT", button_8_drum_name)

    def test_create_drum_name_3(self):
        button_11_drum_name = frame.sound_button_list[10]._text
        self.assertEqual("TOM L", button_11_drum_name)



    # Tests for position() ----------------------------------------
    def test_position_column(self):
        sound_button_column = frame.sound_button_list[4].grid_info()["column"]
        self.assertEqual(4, sound_button_column)

    def test_position_row(self):
        sound_button_row = frame.sound_button_list[11].grid_info()["row"]
        self.assertEqual(0, sound_button_row)

    def test_position_padx(self):
        sound_button_padx = frame.sound_button_list[3].grid_info()["padx"]
        self.assertEqual(SOUND_BUTTON_PAD_X, sound_button_padx)

    def test_position_pady(self):
        sound_button_pady = frame.sound_button_list[9].grid_info()["pady"]
        self.assertEqual(SOUND_BUTTON_PAD_Y, sound_button_pady)