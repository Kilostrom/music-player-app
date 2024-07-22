#  Goals:
# 1. the music player should be able to intake a music playlist and play it
# 2. with the abilities to go next or previous song within the list
import sys
import pygame
import os
import time

# initialize pygame
pygame.init()

# set up the music player
music_player = pygame.mixer_music

# set the directory path for the music files
music_dic = "C:/Users/nengm/Music"

# get a list of music files in the directory
music_files = []

# iterate over the files in the directory
for file in os.listdir(music_dic):
    # check if the file ends with '.mp3'
    if file.endswith('.mp3'):
        music_files.append(file)

# create a GUI window
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Music Player')

# create a font object for displaying text
font = pygame.font.Font(None, 24)

# creating a list to store the current song index
current_song = 0

song_length = 0

song_position = 0


# creating a function to play the next song
def play_next_song():
    global current_song
    global song_length
    global song_position
    current_song = (current_song + 1) % len(music_files)
    music_player.load(os.path.join(music_dic, music_files[current_song]))
    music_player.play()
    song_length = music_player.get_busy() / 1000
    song_position = 0


# create a function to play the previous song
def play_previous_song():
    global current_song
    global song_length
    global song_position
    current_song = (current_song - 1) % len(music_files)
    music_player.load(os.path.join(music_dic, music_files[current_song]))
    music_player.play()
    song_length = music_player.get_busy() / 1000
    song_position = 0


# create a function to play or pause the music
def play_or_pause():
    if music_player.get_busy():
        music_player.pause()
    else:
        music_player.unpause()


# create a function to stop the music
def stop_music():
    music_player.stop()


# create a function to display the current song
def display_current_song():
    song_text = font.render(music_files[current_song], True, (255, 255, 255))
    window.blit(song_text, (20, 20))


# create a function to display the song length
def display_song_length():
    global song_length
    song_length_text = font.render(f'Song Length: {int(song_length)} seconds', True, (255, 255, 255))
    window.blit(song_length_text, (20, 50))


# create a function to display the song position
def display_song_position():
    global song_position
    song_position_text = font.render(f'Song Position: {int(song_position)} seconds', True, (255, 255, 255))
    window.blit(song_position_text, (20, 80))


# main loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_next_song()
            elif event.key == pygame.K_LEFT:
                play_previous_song()
            elif event.key == pygame.K_RIGHT:
                play_next_song()
            elif event.key == pygame.K_ESCAPE:
                stop_music()

    # clear the window
    window.fill((0, 0, 0))

    # display the current song
    display_current_song()
    # display the current song length and position
    display_song_length()
    display_song_position()

    song_position = music_player.get_pos() / 1000

    # update the window
    pygame.display.flip()
    pygame.time.Clock().tick(60)
