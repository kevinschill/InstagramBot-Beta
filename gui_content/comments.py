from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
from tkinter.scrolledtext import ScrolledText

class CommentsTab():
    def __init__(self,gui_frame,database):
        
        self.database = database
        self.main_frame = gui_frame
        self.comments_tab = ttk.Frame(gui_frame)

        gui_frame.add(self.comments_tab, text="Comments")

        self.comments_text = ScrolledText(self.comments_tab,width=100, height=18, wrap=tk.WORD)
        self.comments_text.place(x=0,y=0)
        save_comments_button = Button(self.comments_tab, text="Save",command=lambda: self.save_comments())
        save_comments_button.place(x=5,y=297)

        self.load_comments()
    
    def load_comments(self):
        data = self.database.getComments()
        if data != None:
            for comment in data:
                self.comments_text.insert('insert',str(comment) + "\n")
            self.comments_text.insert("end","")

    def getHandle(self,handle):
        self.database = handle

    def save_comments(self):
        self.database.deleteCommentsToPosts()
        all_comments_text = self.comments_text.get("1.0", "end-1c").split("\n")
        
        self.database.addCommentsToPost(all_comments_text)