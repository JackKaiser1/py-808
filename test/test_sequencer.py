import unittest
from src.sequencer import StepButton, SequencerFrame
from src.constants import *
import customtkinter 

root = customtkinter.CTk()

# class TestStepButton(unittest.TestCase):
#     def test_height(self):
#         step = StepButton(root)
#         self.assertEqual(55, step._height)

class TestSequencerFrame(unittest.TestCase):
    def test_column(self):
        frame = SequencerFrame(root)
        frame.grid(row=0, column=0)
        frame.init_steps()
        frame.position_steps()

        self.assertEqual(3, frame.step_list[4].grid._column)






# if __name__ == "__main__":
#     unittest.main()



root.mainloop()