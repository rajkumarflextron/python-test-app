from moviepy.editor import *
import pygame

def play_audio(file):
    # initialize pygame mixer
    pygame.mixer.init()

    # load the MP3 file
    pygame.mixer.music.load(file)

    # play the MP3 file
    pygame.mixer.music.play()

    # wait for the MP3 file to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
        
def play_video(file):
    # initialize pygame
    pygame.init()

    pygame.display.set_caption('Show Video on screen')

    video = VideoFileClip(file)
    video.preview()



# file="/Users/lk094867/Library/CloudStorage/OneDrive-CernerCorporation/LK/Python_Learnings/Flet_Apps/Learn/assets/test_video.mp4"
# play_video(file)
file="../assets/test_audio.mp3"
play_audio(file)