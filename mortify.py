from tkinter import filedialog
from tkinter import *
import pygame
import os
import random

root = Tk()
root.title('Mortify')
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ''
paused = False

def load_music_preset():
    global current_song
    root.directory = 'Death Metal'

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def load_music_custom():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def nxt_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def shuffle():
    global current_song
    songlist.selection_clear(0, END)
    r = random.randint(1, len(songs))

    if songs.index(current_song) == (len(songs)+1):
        songlist.selection_set(songs.index(current_song) - r)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    elif songs.index(current_song) == 0:
        songlist.selection_set(songs.index(current_song) + r)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    else:
        songlist.selection_set(songs.index(current_song) + r)
        current_song = songs[songlist.curselection()[0]]
        play_music()

def loop():
    global current_song

    while songs.index(current_song) == len(songs):
        songlist.selection_clear(0, END)
        songlist.selection_set(0)
        current_song = songs[songlist.curselection()[0]]
        play_music()

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Death Metal', command=load_music_preset)
organise_menu.add_command(label='Your Playlist', command=load_music_custom)
menubar.add_cascade(label='Playlists', menu=organise_menu)

songlist =  Listbox(root, bg="black", fg="red", width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
nxt_btn_image = PhotoImage(file='play_nxt.png')
prev_btn_image = PhotoImage(file='play_bfr.png')
shuffle_btn_image = PhotoImage(file='shuffle.png')
loop_btn_image = PhotoImage(file='loop.png')
lp1_btn_image = PhotoImage(file='loop_song.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music)
nxt_btn = Button(control_frame, image=nxt_btn_image, borderwidth=0, command=nxt_music)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0, command=prev_music)
shuffle_btn = Button(control_frame, image=shuffle_btn_image, borderwidth=0, command=shuffle)
loop_btn = Button(control_frame, image=loop_btn_image, borderwidth=0, command=loop)
lp1_btn = Button(control_frame, image=lp1_btn_image, borderwidth=0, command=prev_music)

play_btn.grid(row=0, column=3, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
nxt_btn.grid(row=0, column=4, padx=7, pady=10)
prev_btn.grid(row=0, column=1, padx=7, pady=10)
#shuffle_btn.grid(row=0, column=0, padx=7, pady=10)
#loop_btn.grid(row=0, column=5, padx=7, pady=10)
#lp1_btn.grid(row=0, column=6, padx=7, pady=10)

root.mainloop()
