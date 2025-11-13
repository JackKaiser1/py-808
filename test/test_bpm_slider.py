import sys
sys.path.append("/home/jackk/dev/github.com/jackkaiser1/py_808/src")

import unittest
import customtkinter 
from constants import *
from bpm_slider import BPMSliderFrame

root = customtkinter.CTk()
frame = BPMSliderFrame(root)
frame.bpm_slider.set(70)
frame.grid(row=0, column=0)

class TestBPMSliderFrame(unittest.TestCase):
    def test_bpm_slider_label(self):
        self.assertEqual(70, frame.bpm_slider.get())
