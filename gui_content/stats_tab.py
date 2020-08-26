from tkinter import *
from tkinter import ttk
import tkinter as tk

class StatsTab():
    def __init__(self,gui_frame):
        
        self.settings_tab = gui_frame
        self.stats_tab = ttk.Frame(gui_frame)

        gui_frame.add(self.stats_tab, text="Stats")

        self.liked_text = Label(self.stats_tab,text="Photos liked: 0")
        self.liked_text.place(x=5,y=20)

        self.commented_text = Label(self.stats_tab,text="Commented Posts: 0")
        self.commented_text.place(x=5,y=40)

        self.followed_text_stats = Label(self.stats_tab,text="Profiles Followed: 0")
        self.followed_text_stats.place(x=5,y=60)

        self.unfollowed_text_stats = Label(self.stats_tab,text="Profiles Unfollowed: 0")
        self.unfollowed_text_stats.place(x=5,y=80)

        self.comment_feed_text = Label(self.stats_tab,text="Feed Commented: 0")
        self.comment_feed_text.place(x=5,y=100)

        self.accept_text = Label(self.stats_tab,text="Accepted Followers: 0")
        self.accept_text.place(x=5,y=120)

    def setLikedStats(self,text):
        self.liked_text.configure(text=f"Posts Liked: {text}")
    
    def setCommentsStats(self,text):
        self.commented_text.configure(text=f"Comments Posted: {text}")
    
    def setFollowedStats(self,text):
        self.followed_text_stats.configure(text=f"Followed Profiles: {text}")
    
    def setUnfollowedStats(self,text):
        self.unfollowed_text_stats.configure(text=f"Unfollowed Profiles: {text}")
    
    def setCommentFeedStats(self,text):
        self.comment_feed_text.configure(text=f"Commented feed posts: {text}")
    
    def setAcceptedStats(self,text):
        self.accept_text.configure(text=f"Follower Accepted: {text}")



