from tkinter import *
import pygame
import os
from tkinter import messagebox
from tkinter import filedialog
import easygui
import shutil

class MusicPlayer:

  def __init__(self,root):
    self.root = root
    self.root.title("Bootleg IPod Emulator")
    self.root.geometry("350x500")
    pygame.init()
    pygame.mixer.init()
    self.track = StringVar()
    self.status = StringVar()

    def open_window():
       read=easygui.fileopenbox()
       return read

    def playsong():
        try:
           inactive_ticks = 0
           self.track.set(self.playlist.get(ACTIVE))
           self.status.set("-Playing")
           pygame.mixer.music.load(self.playlist.get(ACTIVE))
           pygame.mixer.music.play()
        except:
            msg=messagebox.showerror("ERROR", "Please add Music to Music Folder in ~\Terrible IPod Eimulator\Music")
           

    def stopsong():
        try:
            self.status.set("-Stopped")
            pygame.mixer.music.stop()
        except:
           msg=messagebox.showerror("ERROR", "Opps, There Is an Error While Running :,(")

    def pausesong():
        try:
            self.status.set("-Paused")
            pygame.mixer.music.pause()
        except:
           msg=messagebox.showerror("ERROR", "Opps, There Is an Error While Running :,(")

    def unpausesong():
        try:
            self.status.set("-Playing")
            pygame.mixer.music.unpause()
        except:
           msg=messagebox.showerror("ERROR", "Opps, There Is an Error While Running :,(")
    destination = "c:"
    def repeatsong():
        pygame.mixer.music.play(-1)
        pygame.event.wait()
       


    buttonframe = LabelFrame(self.root,font=("arial",15,"bold"),bg="#5d5e5c",fg="white",relief=GROOVE)
    buttonframe.place(x=75,y=250,width=200,height=190)
    playbtn = Button(buttonframe,text="PAUSE",command=pausesong,width=5,height=2,font=("arial",10,"bold"),fg="white",bg="#5d5e5c").pack(side = LEFT)
    playbtn = Button(buttonframe,text="UNPAUSE",command=unpausesong,width=5,height=2,font=("arial",10,"bold"),fg="white",bg="#5d5e5c").pack(side = RIGHT)
    playbtn = Button(buttonframe,text="PLAY",command=playsong,width=5,height=2,font=("arial",10,"bold"),fg="white",bg="#5d5e5c").pack(side = TOP)
    playbtn = Button(buttonframe,text="Repeat",command=repeatsong,width=11,height=6,font=("arial",10,"bold"),fg="#5d5e5c",bg="white").pack()
    playbtn = Button(buttonframe,text="STOP",command=stopsong,width=5,height=2,font=("arial",10,"bold"),fg="white",bg="#5d5e5c").pack(side=BOTTOM)

    songsframe = LabelFrame(self.root,font=("arial",15,"bold"),bg="white",fg="white",bd=5,relief=GROOVE)
    songsframe.place(x=75,y=30,width=200,height=200)
    scroll_y = Scrollbar(songsframe,orient=VERTICAL)
    self.playlist = Listbox(songsframe,yscrollcommand=scroll_y.set,selectbackground="#B0FC38",selectmode=SINGLE,font=("arial",12,"bold"),bg="#469603",fg="#2b5905",bd=5,relief=GROOVE)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
    os.chdir("Music")
    songtracks = os.listdir()
    for track in songtracks:
      self.playlist.insert(END,track)
    
    


root = Tk()
MusicPlayer(root)

root.resizable(width=0,height=0)
root.configure(bg='white')
root.mainloop()

