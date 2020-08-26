from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font


class UnfollowSettings():
    def __init__(self,gui_frame):

        self.settings_tab = gui_frame

        
        self.unfollow_users_status = IntVar()
        unfollow_users = Checkbutton(self.settings_tab, text="Unfollow Users", variable=self.unfollow_users_status)
        unfollow_users.place(x=220,y=8)

        unfollow_text = Label(self.settings_tab,text="after:")
        unfollow_text.place(x=220,y=30)
        
        self.unfollow_time = Entry(self.settings_tab,width=7)
        self.unfollow_time.place(x=260,y=30)
        self.unfollow_time.insert(0,"")

        unfollow_text_2 = Label(self.settings_tab, text="minutes")
        unfollow_text_2.place(x=300,y=30)

        
            
    def getUnfollowStatus(self):
        return True if self.unfollow_users_status.get() == 1 else False
        
    def getUnfollowMinutes(self):
        return self.unfollow_time.get()

    def setUnfollowMinutes(self,sleepstring):
        self.unfollow_time.insert(0,sleepstring)
