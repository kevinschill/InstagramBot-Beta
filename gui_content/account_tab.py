from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import Font



class AccountTab():
    def __init__(self,gui_frame):

        self.account_tab = ttk.Frame(gui_frame)
        
        myFont = Font(family="Consolas", size=11, weight="normal")

        gui_frame.add(self.account_tab, text="Account")
        
        username_text = tk.Label(self.account_tab, text="Username:")   
        username_text.place(x=100, y=5)
        username_text.configure(font=myFont)

        self.username_input = tk.Entry(self.account_tab)
        self.username_input.place(x=190, y=8)



        password_text = tk.Label(self.account_tab, text="Password:")
        password_text.place(x=100, y=40)
        password_text.configure(font=myFont)

        self.password_text_input = tk.Entry(self.account_tab,show="*")
        self.password_text_input.place(x=190, y=44)

        #username_text_box.insert(0,"bot.mConfig.getUsername()")

        #password_text_box.insert(0,"bot.mConfig.getPassword()")

        self.login_status = tk.Label(self.account_tab, text="Not logged in....")
        self.login_status.place(x=140,y=140)
        self.login_status.configure(font=myFont)
    
    def setUsername(self,text):
        self.username_input.insert(0,text)
    
    def getUsername(self):
        return self.username_input.get()
        
    def setPassword(self,text):
        self.password_text_input.insert(0,text)
    
    def getPassword(self):
        return self.password_text_input.get()
    
    def setLoginStatus(self):
        self.login_status.configure(text="")
        self.login_status.configure(text="Logged in, have fun :)")

