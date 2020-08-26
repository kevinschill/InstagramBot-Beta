from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font


class FollowSetting():
    def __init__(self,gui_frame):

        self.settings_tab = gui_frame

        
        self.follow_users_status = IntVar()
        follow_users = Checkbutton(self.settings_tab, text="Follow Users", variable=self.follow_users_status)
        follow_users.place(x=5,y=190)

        follow_sleep_text = Label(self.settings_tab,text="Sleep for:")
        follow_sleep_text.place(x=5,y=220)

        self.follow_sleep = Entry(self.settings_tab,width=7)
        self.follow_sleep.place(x=60,y=220)
        self.follow_sleep.insert(0,"")
    
    def getFollowStatus(self):
        return True if self.follow_users_status.get() == 1 else False

    def getFollowSleepText(self):
        return self.follow_sleep.get()

    def getFollowSleepReal(self):
        temp_sleep = self.follow_sleep.get().split(",")
        return int(temp_sleep[0]),int(temp_sleep[1])
    
    def setFollowSleep(self,sleepstring):
        self.follow_sleep.insert(0,sleepstring)
    





