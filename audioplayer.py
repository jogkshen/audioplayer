import tkinter as tk
from tkinter import filedialog
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player By Jogkshen")
canvas.geometry("400x500")
canvas.config(bg="black")

#rootpath = "D:\\geetharu tapaiko\\Anil Singh"
#pattern = "*.mp3"

mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir='audio/',filetype =(("mp3files","*.mp3"),))
    print(song)

    #song=song.replace("C:/Music/","")
    #song=song.replace(".mp3","")
    listBox.insert('end', song)
      
def select():
    song=listBox.get("anchor")
    #song=f'C:/Music/{song}.mp3'
    mixer.music.load(song)

    #label.config(text = listBox.get("anchor"))
    #mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def next():
    next_song=listBox.curselection()
    next_song= next_song[0]+1
    next_song_name = listBox.get(next_song)
    label.config(text= next_song_name)
    mixer.music.load(next_song_name)
    #mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def previous():
    previous_song=listBox.curselection()
    previous_song= previous_song[0]-1
    previous_song_name = listBox.get(previous_song)
    label.config(text= previous_song_name)
    mixer.music.load(previous_song_name)
    #mixer.music.load(rootpath + "\\" + previous_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(previous_song)
    listBox.select_set(previous_song)


def pause():
    if pause_button["text"] == "pause":
                    mixer.music.pause()
                    pause_button["text"] = "play"
    else:
        mixer.music.unpause()
        pause_button["text"] ="pause"

        
    
listBox= tk.Listbox(canvas, fg="cyan", bg="black", width=100)
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', bg="black", fg="red")
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor = 'center')

Add_song= tk.Button(canvas, text="add song", bg="white", command = add_song)
Add_song.pack(pady=25, in_=top,side='left')

play_button = tk.Button(canvas, text="play", bg="green", command = select)
play_button.pack(pady=25, in_ = top,side = 'left')

pause_button = tk.Button(canvas, text="pause", bg="yellow", command= pause)
pause_button.pack(pady=25, in_ = top,side = 'left')

previous_button = tk.Button(canvas, text="previous", bg="blue", command = previous)
previous_button.pack(pady=25, in_ = top,side = 'left')

next_button = tk.Button(canvas, text="next", bg="blue", command= next)
next_button.pack(pady=25, in_ = top,side = 'left')

stop_button = tk.Button(canvas, text="stop", bg="red", command= stop)
stop_button.pack(pady=25, in_ = top,side = 'left')




#for root, dirs, files in os.walk(rootpath):
    #for filename in fnmatch.filter(files, pattern):
        #listBox.insert('end', filename)

canvas.mainloop()
