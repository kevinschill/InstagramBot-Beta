import json
import random
from datetime import datetime

class ConfigLoader():

    def ReadConfig(self):
        self.hashtags = []
        self.comments = []

        with open("settings.json") as jsonfile:
            data = json.load(jsonfile)
            for key, value in data.items():
                if key == "likestoday":
                    self.likestoday = int(value)
                if key == "commentstoday":
                    self.commentstoday = int(value)
                if key == "username":
                    self.username = value
                if key == "password":
                    self.password = value
                if key == "sleeplike":
                    self.sleeplike = value
                if key == "sleepfollow":
                    self.sleepfollow = value
                if key == "sleepcomment":
                    self.sleepcomment = value
                if key == "sleepacceptfollower":
                    self.sleepacceptfollower = value
                if key == "sleepcommentmyfeed":
                    self.sleepcommentmyfeed = value
                if key == "unfollowtimer":
                    self.unfollowtimer = value

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getLikeSleep(self):
       return self.sleeplike

    def getCommentSleep(self):
        return self.sleepcomment

    def getFollowSleep(self):
        return self.sleepfollow

    def getUnfollowTime(self):
        return self.unfollowtimer
    
    def getAcceptFollowerTime(self):
        return self.sleepacceptfollower
    
    def getCommentMyFeedTime(self):
        return self.sleepcommentmyfeed