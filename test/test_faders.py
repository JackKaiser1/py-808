import sys
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
import customtkinter 
from constants import *
from faders import VolumeFaderFrame
from sound_mixer import drum_rack

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


    # Test init_command and set_command 
    def test_set_command_fader_1(self):
        fader_command_1 = frame.fader_list[6]._command
        self.assertIsNotNone(fader_command_1)

    def test_set_command_fader_2(self):
        fader_command_2 = frame.fader_list[15]._command
        self.assertIsNotNone(fader_command_2)

    
    # Test set_volume 
    def test_set_volume_1(self):
        frame.set_volume(0.2, drum_rack.rim)
        rim_volume = drum_rack.rim.volume
        self.assertEqual(0.2, rim_volume)
        
        frame.set_volume(0.5, drum_rack.rim)

    def test_set_volume_2(self):
        frame.set_volume(0.8, drum_rack.clap)
        clap_volume = drum_rack.clap.volume
        self.assertEqual(0.8, clap_volume)
        
        frame.set_volume(0.5, drum_rack.clap)

    def test_set_volume_3(self):
        frame.set_volume(0.8, drum_rack.clap)
        frame.set_volume(0.2, drum_rack.clap)
        frame.set_volume(1, drum_rack.clap)
        clap_volume = drum_rack.clap.volume
        self.assertEqual(1, clap_volume)

        frame.set_volume(0.5, drum_rack.clap)

    def test_set_volume_4(self):
        frame.set_volume(0.2, drum_rack.rim)
        frame.set_volume(0.9, drum_rack.rim)
        frame.set_volume(0.4, drum_rack.rim)
        rim_volume = drum_rack.rim.volume
        self.assertEqual(0.4, rim_volume)
        
        frame.set_volume(0.5, drum_rack.rim)


