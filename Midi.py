import pygame.midi
import time

class Midi :
     def __init__(self):
          pygame.mixer.init()

     def playNote(self, note):
        if note > 23 :
            pygame.mixer.music.load('DO1.mp3')
            pygame.mixer.music.play()
            time.sleep(0.5)
            pygame.mixer.music.stop
            print('do')
        elif note < 23 and note > 18 :
            pygame.mixer.music.load('RE.mp3')
            pygame.mixer.music.play()
            time.sleep(0.5)
            pygame.mixer.music.stop
            print('re')
        elif note < 18 and note > 13 :
            pygame.mixer.music.load('MI.mp3')
            pygame.mixer.music.play()
            time.sleep(0.5)
            pygame.mixer.music.stop
            print('mi')
        elif note < 13 and note > 8 :
            pygame.mixer.music.load('FA.mp3')
            pygame.mixer.music.play()
            time.sleep(0.5)
            pygame.mixer.music.stop
            print('fa')
        elif note == 7 :
            pygame.mixer.music.load('SOL.mp3')
            pygame.mixer.music.play()
            time.sleep(0.5)
            pygame.mixer.music.stop
            print('sol')
        elif note < 3 :
            pygame.mixer.music.load('RA.mp3')
            pygame.mixer.music.play()
            time.sleep(0.5)
            pygame.mixer.music.stop
            print('ra')
        elif note == "SI" :
            pygame.mixer.music.load('SI.mp3')
            pygame.mixer.music.play()
            time.sleep(0.5)
            pygame.mixer.music.stop
        elif note == "DO2" :
            pygame.mixer.music.load('DO2.mp3')
            pygame.mixer.music.play()
            time.sleep(0.5)
            pygame.mixer.music.stop
