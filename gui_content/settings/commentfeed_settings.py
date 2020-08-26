from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font


class CommentFeedSettings():
    def __init__(self,gui_frame):

        self.settings_tab = gui_frame

        self.comment_my_feed_value = IntVar()
        comment_my_feed = Checkbutton(self.settings_tab, text="Comment my Feed", variable=self.comment_my_feed_value).place(x=220,y=125)

        comment_my_feed_text = Label(self.settings_tab,text="Sleep for:").place(x=220,y=155)

        self.comment_my_feed_box = Entry(self.settings_tab,width=7)
        self.comment_my_feed_box.place(x=280,y=155)
        self.comment_my_feed_box.insert(0,"")
    
    def getCommentFeedStatus(self):
        return True if self.comment_my_feed_value.get() == 1 else False

    def getCommentFeedSleep(self):
        return self.comment_my_feed_box.get()

    def getCommentFeedReal(self):
        temp_sleep = self.comment_my_feed_box.get().split(",")
        return int(temp_sleep[0]),int(temp_sleep[1])
    
    def setCommentFeedSleep(self,sleepstring):
        self.comment_my_feed_box.insert(0,sleepstring)

