import pygame
from pygame import mixer
from sound_class import counter, drum
from assets import *
# from drum_obj_dict import drum_obj_dict
# from play_pause import PlayButton
from sound_class import DrumSample

pygame.mixer.init(channels=1)
pygame.mixer.set_num_channels(16)

class DrumRack():
    def __init__(self):
        
        # Init DrumSample objects ---------------------------------
        self.kick = DrumSample("assets/Kick Short.wav")
        self.snare = DrumSample("assets/Snare Bright.wav")
        self.clap = DrumSample("assets/Clap.wav")
        self.hihat = DrumSample("assets/Hihat.wav")
        self.rim = DrumSample("assets/Rimshot.wav")
        self.cowbell = DrumSample("assets/Cowbell.wav")
        self.crash = DrumSample("assets/Cymbal.wav")
        self.open_hat = DrumSample("assets/Open Hat Short.wav")
        self.maracas = DrumSample("assets/Maracas.wav")
        self.clav = DrumSample("assets/Claves.wav")
        self.tom_low = DrumSample("assets/Tom Low.wav")
        self.tom_mid = DrumSample("assets/Tom Mid.wav")
        self.tom_hi = DrumSample("assets/Tom High.wav")
        self.conga_low = DrumSample("assets/Conga Low.wav")
        self.conga_mid = DrumSample("assets/Conga Mid.wav")
        self.conga_hi = DrumSample("assets/Conga High.wav")

        # Init channels -------------------------------------------
        self.channel_0 = pygame.mixer.Channel(0)
        self.channel_1 = pygame.mixer.Channel(1)
        self.channel_2 = pygame.mixer.Channel(2)
        self.channel_3 = pygame.mixer.Channel(3)
        self.channel_4 = pygame.mixer.Channel(4)
        self.channel_5 = pygame.mixer.Channel(5)
        self.channel_6 = pygame.mixer.Channel(6)
        self.channel_7 = pygame.mixer.Channel(7)
        self.channel_8 = pygame.mixer.Channel(8)
        self.channel_9 = pygame.mixer.Channel(9)
        self.channel_10 = pygame.mixer.Channel(10)
        self.channel_11 = pygame.mixer.Channel(11)
        self.channel_12 = pygame.mixer.Channel(12)
        self.channel_13 = pygame.mixer.Channel(13)
        self.channel_14 = pygame.mixer.Channel(14)
        self.channel_15 = pygame.mixer.Channel(15)

        # Init drum object dictionary
        self.drum_obj_dict = {self.kick : self.play_kick,
                              self.snare : self.play_snare,
                              self.clap : self.play_clap,
                              self.hihat : self.play_hihat, 
                              self.rim : self.play_rim,
                              self.cowbell : self.play_cowbell,
                              self.crash : self.play_cymbal,
                              self.open_hat : self.play_open_hat,
                              self.maracas : self.play_maracas,
                              self.clav : self.play_claves,
                              self.tom_low : self.play_tom_low,
                              self.tom_mid : self.play_tom_mid,
                              self.tom_hi : self.play_tom_hi,
                              self.conga_low : self.play_conga_low,
                              self.conga_mid : self.play_conga_mid,
                              self.conga_hi : self.play_conga_hi,}

    # Advances step sequencer - called in loop by play button
    def loop(self):
        played_sounds = []
        counter.count += 1
        for drum_obj in self.drum_obj_dict.keys():
            if counter.count in drum_obj.beat_list:
                self.drum_obj_dict[drum_obj]()
                played_sounds.append(drum_obj.beat_list)

        if counter.count == 16:
            counter.count = 0

        return played_sounds

    # Play methods
    def play_kick(self):
        self.channel_0.set_volume(self.kick.volume)
        self.channel_0.play(self.kick)
    def play_snare(self):
        self.channel_1.set_volume(self.snare.volume)
        self.channel_1.play(self.snare)
    def play_clap(self):
        self.channel_2.set_volume(self.clap.volume)
        self.channel_2.play(self.clap)
    def play_hihat(self):
        self.channel_3.set_volume(self.hihat.volume)
        self.channel_3.play(self.hihat)
    def play_rim(self):
        self.channel_4.set_volume(self.rim.volume)
        self.channel_4.play(self.rim)
    def play_cowbell(self):
        self.channel_5.set_volume(self.cowbell.volume)
        self.channel_5.play(self.cowbell)
    def play_cymbal(self):
        self.channel_6.set_volume(self.crash.volume)
        self.channel_6.play(self.crash)
    def play_open_hat(self):
        self.channel_7.set_volume(self.open_hat.volume)
        self.channel_7.play(self.open_hat)
    def play_maracas(self):
        self.channel_8.set_volume(self.maracas.volume)
        self.channel_8.play(self.maracas)
    def play_claves(self):
        self.channel_9.set_volume(self.clav.volume)
        self.channel_9.play(self.clav)
    def play_tom_low(self):
        self.channel_10.set_volume(self.tom_low.volume)
        self.channel_10.play(self.tom_low)
    def play_tom_mid(self):
        self.channel_11.set_volume(self.tom_mid.volume)
        self.channel_11.play(self.tom_mid)
    def play_tom_hi(self):
        self.channel_12.set_volume(self.tom_hi.volume)
        self.channel_12.play(self.tom_hi)
    def play_conga_low(self):
        self.channel_13.set_volume(self.conga_low.volume)
        self.channel_13.play(self.conga_low)
    def play_conga_mid(self):
        self.channel_14.set_volume(self.conga_mid.volume)
        self.channel_14.play(self.conga_mid)
    def play_conga_hi(self):
        self.channel_15.set_volume(self.conga_hi.volume)
        self.channel_15.play(self.conga_hi)

    
drum_rack = DrumRack()

