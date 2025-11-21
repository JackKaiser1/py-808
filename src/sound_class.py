import pygame 
from pygame import mixer
# from drum_rack import *

class DrumSample(pygame.mixer.Sound):
    def __init__(self, filename):
        super().__init__(filename)
        self.beat_list = set()
        self.filename = filename


class Counter():
    def __init__(self):
        self.count = 0


class Drum():
    def __init__(self):
        self.current_drum = None


counter = Counter()
drum = Drum()

