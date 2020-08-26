from tkinter import *
from tkinter import ttk
import tkinter as tk
from gui_content.settings.like_settings import LikeSettings
from gui_content.settings.comment_settings import CommentSettings
from gui_content.settings.follow_settings import FollowSetting
from gui_content.settings.unfollow_settings import UnfollowSettings
from gui_content.settings.acceptfollowers_settings import AcceptfollowersSetting
from gui_content.settings.commentfeed_settings import CommentFeedSettings

import json

class SettingsTab():
    def __init__(self,gui_frame):
        
        self.main_frame = gui_frame
        self.settings_tab = ttk.Frame(gui_frame)

        gui_frame.add(self.settings_tab, text="Settings")

        self.like_settings = LikeSettings(self.settings_tab)

        self.comment_settings = CommentSettings(self.settings_tab)

        self.follow_settings = FollowSetting(self.settings_tab)

        self.unfollow_settings = UnfollowSettings(self.settings_tab)

        self.acceptfollowers_settings = AcceptfollowersSetting(self.settings_tab)

        self.commentfeed_settings = CommentFeedSettings(self.settings_tab)

        settings_save_button = Button(self.settings_tab, text="Save Setting",command=lambda: self.save_settings())
        settings_save_button.place(x=5,y=260)
    
    def save_settings(self):
        with open("settings.json") as oldfile:
                data = json.load(oldfile)

        data["likestoday"] = self.like_settings.getMaxLikesToday()
        data["commentstoday"] = self.comment_settings.getMaxCommentsToday()
        data["sleeplike"] = self.like_settings.getLikeSleepText()
        data["sleepcomment"] = self.comment_settings.getCommentSleepText()
        data["sleepfollow"] = self.follow_settings.getFollowSleepText()
        data["sleepacceptfollower"] = self.acceptfollowers_settings.getAcceptfollowersSleepText()
        data["sleepcommentmyfeed"] = self.commentfeed_settings.getCommentFeedSleep()
        data["unfollowtimer"] = self.unfollow_settings.getUnfollowMinutes()
        
        with open("settings.json", "w+") as newfile:
            json.dump(data, newfile, indent=4)

