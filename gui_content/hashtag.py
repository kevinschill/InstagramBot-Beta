from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
from tkinter.scrolledtext import ScrolledText

class HashtagTab():
    def __init__(self,gui_frame,database):
        
        self.database = database
        self.main_frame = gui_frame
        self.hashtag_tab = ttk.Frame(gui_frame)

        gui_frame.add(self.hashtag_tab, text="Hashtags")


        self.hashtags_text = ScrolledText(self.hashtag_tab,width=100, height=18, wrap=tk.WORD)
        self.hashtags_text.place(x=0,y=0)
        save_hashtags_btn = tk.Button(self.hashtag_tab, text="Save",command=lambda: self.save_hashtags())
        save_hashtags_btn.place(x=5,y=297)

        self.load_hashtags()

    def load_hashtags(self):
        data = self.database.getHashtags()
        if data != None:
            for hashtag in data:
                self.hashtags_text.insert('insert',str(hashtag) + "\n")
            self.hashtags_text.insert("end","")

    def getHandle(self,handle):
        self.database = handle

    def save_hashtags(self):
        self.database.deleteHashtag()
        all_hashtags_text = self.hashtags_text.get("1.0", "end-1c").split("\n")

        self.database.addHashtags(all_hashtags_text)