from tkinter import *
from tkinter import ttk
import tkinter as tk
import os

from gui_content.settings_tab import SettingsTab
from gui_content.log_tab import LogTab
from gui_content.account_tab import AccountTab
from gui_content.stats_tab import StatsTab
from gui_content.comments import CommentsTab
from gui_content.hashtag import HashtagTab

from ConfigLoader import ConfigLoader

from tkinter.font import Font
import webbrowser

class MainGui():
    def __init__(self,BotHandle=None):
        super().__init__()

        self.botHandle = BotHandle
        self.config = ConfigLoader()
        self.config.ReadConfig()

        self.handle = Tk()
        self.handle.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.handle.geometry('500x350')
        self.handle.title("InstagramBot 2020")
        self.handle.resizable(False, False)

        self.tab_main = ttk.Notebook(self.handle)
        
        self.account_tab = AccountTab(self.tab_main)

        self.settings_tab = SettingsTab(self.tab_main)

        self.comments_tab = CommentsTab(self.tab_main,self.botHandle.getDatabaseHandle())

        self.hashtag_tab = HashtagTab(self.tab_main,self.botHandle.getDatabaseHandle())

        self.stats_tab = StatsTab(self.tab_main)

        self.log_tab = LogTab(self.tab_main)

        self.donate_tab = ttk.Frame(self.tab_main)

        self.tab_main.add(self.donate_tab, text="Donation")

        def openweb():
            webbrowser.open("https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=Q8EANTRLUBWZ6&source=url",new=1)
        photo = PhotoImage(file = "webdrivers/etc/paypal.png")
        

        Btn = Button(self.donate_tab, text = "Click me",image = photo,compound = BOTTOM, command=openweb)
        Btn.image = photo

        Btn.place(x=140,y=100)
        
        self.setupAccount()
        
        self.loadSettings()

        self.botHandle.getGuiHandle(self)



        self.temp_ban_text = tk.Label(self.account_tab.account_tab, text="Temp Ban: False")
        self.temp_ban_text.place(x=150,y=280)
        self.temp_ban_text.configure(font=Font(family="Consolas", size=11, weight="normal"))

        self.tab_main.pack(expand=1, fill='both')

    def withdraw_window(self,x = None):
        self.handle.destroy()
        os._exit(1)

    def AccountLogin(self):
        self.botHandle.Login()
    
    def AccountStartBot(self):
        self.botHandle.bot_running = True

    def AccountStopBot(self):
        self.botHandle.bot_running = False

    def setupAccount(self):
        login_button = tk.Button(self.account_tab.account_tab, text="Login",command=lambda: self.AccountLogin())
        login_button.place(x=100,y=90)

        stop_button = tk.Button(self.account_tab.account_tab, text="Start",command=lambda: self.AccountStartBot())
        stop_button.place(x=190,y=90)

        stop_button = tk.Button(self.account_tab.account_tab, text="Stop",command=lambda: self.AccountStopBot())
        stop_button.place(x=280,y=90)
        browser_choice = IntVar(value=2)

        


    def loadSettings(self):
        self.account_tab.setUsername(self.config.getUsername())
        self.account_tab.setPassword(self.config.getPassword())

        self.settings_tab.like_settings.setMaxLikesToday(self.config.likestoday)
        self.settings_tab.like_settings.setLikeSleep(self.config.getLikeSleep())

        self.settings_tab.comment_settings.setMaxCommentsToday(self.config.commentstoday)
        self.settings_tab.comment_settings.setCommentSleep(self.config.getCommentSleep())

        self.settings_tab.follow_settings.setFollowSleep(self.config.getFollowSleep())

        self.settings_tab.unfollow_settings.setUnfollowMinutes(self.config.getUnfollowTime())

        self.settings_tab.acceptfollowers_settings.setAcceptfollowersSleepText(self.config.getAcceptFollowerTime())

        self.settings_tab.commentfeed_settings.setCommentFeedSleep(self.config.getCommentMyFeedTime())

        

    def start_gui(self):
        self.handle.mainloop()