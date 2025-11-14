import pygame 
from pygame import mixer

class DrumSample(pygame.mixer.Sound):
    def __init__(self, filename):
        super().__init__(filename)
        self.beats = [set()]
        self.filename = filename

class Counter():
    def __init__(self):
        self.count = 0