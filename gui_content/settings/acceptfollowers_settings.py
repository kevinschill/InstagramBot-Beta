from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font


class AcceptfollowersSetting():
    def __init__(self,gui_frame):

        self.settings_tab = gui_frame

        
        self.accept_followsers_value = IntVar()
        accept_followsers = Checkbutton(self.settings_tab, text="Accept Followers", variable=self.accept_followsers_value)
        accept_followsers.place(x=220,y=70)

        accept_followsers_text = Label(self.settings_tab,text="Sleep for:").place(x=220,y=100)

        self.accept_followsers_box = Entry(self.settings_tab,width=7)
        self.accept_followsers_box.place(x=280,y=100)
        self.accept_followsers_box.insert(0,"")
    
    def getAcceptfollowersStatus(self):
        return True if self.accept_followsers_value.get() == 1 else False

    def getAcceptfollowersSleepText(self):
        return self.accept_followsers_box.get()

    def getAcceptfollowersSleepReal(self):
        temp_sleep = self.accept_followsers_box.get().split(",")
        return int(temp_sleep[0]),int(temp_sleep[1])
    
    def setAcceptfollowersSleepText(self,sleepstring):
        self.accept_followsers_box.insert(0,sleepstring)
