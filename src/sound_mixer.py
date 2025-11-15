import pygame
from pygame import mixer
# from sound_class import DrumSample, Counter
from assets import *

class DrumSample(pygame.mixer.Sound):
    def __init__(self, filename):
        super().__init__(filename)
        self.beat_list = set()
        self.filename = filename

# Init pygame mixer
pygame.mixer.init(channels=1)
pygame.mixer.set_num_channels(16)

# Init DrumSample objects
kick = DrumSample("assets/Kick Short.wav")
snare = DrumSample("assets/Snare Bright.wav")
clap = DrumSample("assets/Clap.wav")
hihat = DrumSample("assets/Hihat.wav")
rim = DrumSample("assets/Rimshot.wav")
cowbell = DrumSample("assets/Cowbell.wav")
crash = DrumSample("assets/Cymbal.wav")
open_hat = DrumSample("assets/Open Hat Short.wav")
maracas = DrumSample("assets/Maracas.wav")
clav = DrumSample("assets/Claves.wav")
tom_low = DrumSample("assets/Tom Low.wav")
tom_mid = DrumSample("assets/Tom Mid.wav")
tom_hi = DrumSample("assets/Tom High.wav")
conga_low = DrumSample("assets/Conga Low.wav")
conga_mid = DrumSample("assets/Conga Mid.wav")
conga_hi = DrumSample("assets/Conga High.wav")

# Init sound channels
channel_0 = pygame.mixer.Channel(0)
channel_1 = pygame.mixer.Channel(1)
channel_2 = pygame.mixer.Channel(2)
channel_3 = pygame.mixer.Channel(3)
channel_4 = pygame.mixer.Channel(4)
channel_5 = pygame.mixer.Channel(5)
channel_6 = pygame.mixer.Channel(6)
channel_7 = pygame.mixer.Channel(7)
channel_8 = pygame.mixer.Channel(8)
channel_9 = pygame.mixer.Channel(9)
channel_10 = pygame.mixer.Channel(10)
channel_11 = pygame.mixer.Channel(11)
channel_12 = pygame.mixer.Channel(12)
channel_13 = pygame.mixer.Channel(13)
channel_14 = pygame.mixer.Channel(14)
channel_15 = pygame.mixer.Channel(15)

class Counter():
    def __init__(self):
        self.count = 0

class Drum():
    def __init__(self):
        self.current_drum = kick

# Init drum and counter objects
counter = Counter()
drum = Drum()

def play_kick():
    channel_0.play()
def play_snare():
    channel_1.play()
def play_clap():
    channel_2.play()
def play_hihat():
    channel_3.play()
def play_rim():
    channel_4.play()
def play_cowbell():
    channel_5.play()
def play_cymbal():
    channel_6.play()
def play_open_hat():
    channel_7.play()
def play_maracas():
    channel_8.play()
def play_claves():
    channel_9.play()
def play_tom_low():
    channel_10.play()
def play_tom_mid():
    channel_11.play()
def play_tom_hi():
    channel_12.play()
def play_conga_low():
    channel_13.play()
def play_conga_mid():
    channel_14.play()
def play_conga_hi():
    channel_15.play()


def play():
    while True:
        key = input()
        if key == "e":
            channel_0.play(conga_hi)
        else: 
            break






