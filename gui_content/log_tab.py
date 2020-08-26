from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font
from datetime import datetime

class LogTab():
    def __init__(self,gui_frame):

        log_tab = ttk.Frame(gui_frame)

        gui_frame.add(log_tab, text="Log")
        
        self.log_text = ScrolledText(log_tab,width=125, height=32, wrap=tk.WORD)
        self.log_text.place(x=0,y=0)
        self.log_text.configure(font=Font(family="Consolas", size=7, weight="normal"),state='disabled')

    def getHandle(self):
        return self

    def writeLog(self,text):
        self.log_text.configure(state='normal')
        self.log_text.insert('insert',datetime.now().strftime("[%d/%m/%Y %H:%M:%S]") + " | " + text + "\n")
        self.log_text.configure(state='disabled')