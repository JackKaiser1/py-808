import sys 
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
from unittest.mock import patch, MagicMock
import customtkinter
from sound_select import SoundSelectFrame
from constants import *
from sound_mixer import *
from sequencer import SequencerFrame
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

        # Position frames
        self.sequencer.grid(row=3, column=0, pady=10)
        self.sound_select_buttons.grid(row=2, column=0, pady=10)

        # Center widgets in column 0
        self.grid_columnconfigure(0, weight=1)

root = TestRoot()
root.withdraw()

root.sequencer.create()
root.sound_select_buttons.create(root)

class TestSoundSelectFrame(unittest.TestCase):

    # Tests for create() ----------------------------------------
    def test_create_drum_name_1(self):
        button_4_drum_name = root.sound_select_buttons.sound_buttons[3]._text
        self.assertEqual("HHAT", button_4_drum_name)

    def test_create_drum_name_2(self):
        button_8_drum_name = root.sound_select_buttons.sound_buttons[7]._text
        self.assertEqual("OHAT", button_8_drum_name)

    def test_create_drum_name_3(self):
        button_11_drum_name = root.sound_select_buttons.sound_buttons[10]._text
        self.assertEqual("TOM L", button_11_drum_name)



    # Tests for position() ----------------------------------------
    def test_position_column(self):
        sound_button_column = root.sound_select_buttons.sound_buttons[4].grid_info()["column"]
        self.assertEqual(4, sound_button_column)

    def test_position_row(self):
        sound_button_row = root.sound_select_buttons.sound_buttons[11].grid_info()["row"]
        self.assertEqual(0, sound_button_row)

    def test_position_padx(self):
        sound_button_padx = root.sound_select_buttons.sound_buttons[3].grid_info()["padx"]
        self.assertEqual(SOUND_BUTTON_PAD_X, sound_button_padx)

    def test_position_pady(self):
        sound_button_pady = root.sound_select_buttons.sound_buttons[9].grid_info()["pady"]
        self.assertEqual(SOUND_BUTTON_PAD_Y, sound_button_pady)


    # Test init_command and set_command
    def test_set_command_1(self):
        sound_button_command_1 = root.sound_select_buttons.sound_buttons[4]._command
        self.assertIsNotNone(sound_button_command_1)

    def test_set_command_2(self):
        sound_button_command_2 = root.sound_select_buttons.sound_buttons[8]._command
        self.assertIsNotNone(sound_button_command_2)

    # Test drum_select
    # ----- Test current drum
    def test_select_drum_snare(self):
        snare_button = root.sound_select_buttons.sound_buttons[1]
        root.sound_select_buttons.select_drum(snare_button, root)

        current_drum = drum.current_drum
        
        self.assertEqual(drum_rack.snare, current_drum)

    def test_select_drum_hihat(self):
        hihat_button = root.sound_select_buttons.sound_buttons[3]
        root.sound_select_buttons.select_drum(hihat_button, root)

        current_drum = drum.current_drum
        
        self.assertEqual(drum_rack.hihat, current_drum)

    def test_select_drum_tom_hi(self):
        tom_hi_button = root.sound_select_buttons.sound_buttons[12]
        root.sound_select_buttons.select_drum(tom_hi_button, root)

        current_drum = drum.current_drum
        
        self.assertEqual(drum_rack.tom_hi, current_drum)

    # ----- Test activate_button
    def test_activate_button_snare(self):
        snare_button = root.sound_select_buttons.sound_buttons[1]
        root.sound_select_buttons.select_drum(snare_button, root)

        self.assertEqual(ORANGE_1, snare_button._fg_color)

    def test_activate_button_hihat(self):
        hihat_button = root.sound_select_buttons.sound_buttons[3]
        root.sound_select_buttons.select_drum(hihat_button, root)

        self.assertEqual(ORANGE_1, hihat_button._fg_color) 

    def test_activate_button_tom_hi(self):
        tom_hi_button = root.sound_select_buttons.sound_buttons[12]
        root.sound_select_buttons.select_drum(tom_hi_button, root)

        self.assertEqual(ORANGE_1, tom_hi_button._fg_color) 


         
    
