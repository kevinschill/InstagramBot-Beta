from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font


class LikeSettings():
    def __init__(self,gui_frame):

        self.settings_tab = gui_frame

        likes_today_text = tk.Label(self.settings_tab, text="max. Likes Today : ")
        likes_today_text.place(x=5, y=5)
        
        self.likes_today_text_entry = tk.Entry(self.settings_tab,width=7)
        self.likes_today_text_entry.place(x=140, y=8)
        self.likes_today_text_entry.insert(0,"")

        self.like_random_status = IntVar()
        self.like_random = Checkbutton(self.settings_tab, text="Like Photos", variable=self.like_random_status).place(x=5,y=30)

        like_sleep_text = Label(self.settings_tab,text="Sleep for : ")
        like_sleep_text.place(x=5,y=60)

        self.like_sleep = Entry(self.settings_tab,width=8)
        self.like_sleep.place(x=65,y=60)
        self.like_sleep.insert(0,"")
    
    def getLikeStatus(self):
        return True if self.like_random_status.get() == 1 else False

    def getMaxLikesToday(self):
        return self.likes_today_text_entry.get()

    def setMaxLikesToday(self,string):
        self.likes_today_text_entry.insert(0,string)

    def getLikeSleepText(self):
        return self.like_sleep.get()

    def getLikeSleepReal(self):
        temp_sleep = self.like_sleep.get().split(",")
        return int(temp_sleep[0]),int(temp_sleep[1])
    
    def setLikeSleep(self,sleepstring):
        self.like_sleep.insert(0,sleepstring)

