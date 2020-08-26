from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font


class CommentSettings():
    def __init__(self,gui_frame):

        self.settings_tab = gui_frame

        comments_today_text = tk.Label(self.settings_tab, text="max. Comments Today:")
        comments_today_text.place(x=5, y=100)

        self.comments_today_entry = tk.Entry(self.settings_tab,width=7)
        self.comments_today_entry.place(x=140, y=102)
        self.comments_today_entry.insert(0,"")

    
        self.comment_random_status = IntVar()
        comment_random = Checkbutton(self.settings_tab, text="Comment Photos", variable=self.comment_random_status)
        comment_random.place(x=5,y=125)

        comment_sleep_text = Label(self.settings_tab,text="Sleep for:")
        comment_sleep_text.place(x=5,y=155)

        self.comment_sleep = Entry(self.settings_tab,width=8)
        self.comment_sleep.place(x=65,y=155)
        self.comment_sleep.insert(0,"")
    
    def getCommentStatus(self):
        return True if self.comment_random_status.get() == 1 else False

    def getMaxCommentsToday(self):
        return self.comments_today_entry.get()

    def setMaxCommentsToday(self,string):
        self.comments_today_entry.insert(0,string)

    def getCommentSleepText(self):
        return self.comment_sleep.get()

    def getCommentSleepReal(self):
        temp_sleep = self.comment_sleep.get().split(",")
        return int(temp_sleep[0]),int(temp_sleep[1])
    
    def setCommentSleep(self,sleepstring):
        self.comment_sleep.insert(0,sleepstring)
    

