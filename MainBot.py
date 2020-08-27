from database import Datenbank
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import selenium

import sys, os, time
import random

class MainBot():
    def __init__(self):
        super().__init__()

        self.database = Datenbank()

        self.guiHandle = 0

        self.browser = 0




        self.liked_posts_count = 0
        self.commented_posts_count = 0
        self.followed_count = 0
        self.unfollowed_counter = 0


        self.loggedIn = False
        self.bot_running = False

        self.temp_banned = False
    
    def setupDatabase(self):
        self.database = Datenbank()
        
    def WaitForObject(self, type, string,function_call):
        try:
            return selenium.webdriver.support.ui.WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((type, string)))
        except Exception as error:
            with open("errorlog.txt","a") as errorfile:
                finalmsg = "[{}] Function[{}] Message: {}\n".format(datetime.now().strftime("%d-%m-%Y / %H:%M:%S"),function_call,error)
                errorfile.write(finalmsg)
            return False

    def WaitForObjectNoLog(self, type, string):
        try:
            return selenium.webdriver.support.ui.WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((type, string)))
        except Exception as error: 
            return False

    def WaitForObjects(self, type, string,function_call):
        try:
            return selenium.webdriver.support.ui.WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((type, string)))
        except Exception as error:
            with open("errorlog.txt","a") as errorfile:
                finalmsg = "[{}] Function[{}] Message: {}\n".format(datetime.now().strftime("%d-%m-%Y / %H:%M:%S"),function_call,error)
                errorfile.write(finalmsg)
            return False

    def getDatabaseHandle(self):
        return self.database

    def getGuiHandle(self,handle):
        self.guiHandle = handle

    def Log(self,text):
        self.guiHandle.log_tab.writeLog(text)

    def check_following_time(self,timestamp_):
        followed_time = datetime.strptime(timestamp_, "%d-%m-%Y / %H:%M:%S")
        time_now = datetime.strptime(datetime.now().strftime("%d-%m-%Y / %H:%M:%S"), "%d-%m-%Y / %H:%M:%S")

        td_mins = int(round(abs((followed_time - time_now).total_seconds()) / 60))

        if td_mins >= self.guiHandle.settings_tab.unfollow_settings.getUnfollowMinutes(): # 1 Std
            return True
        else:
            return False

    def Login(self):

        self.Log("Start browser...")
        
        opts = selenium.webdriver.chrome.options.Options()
        opts.add_argument('--disable-infobars')
        opts.add_argument('--headless')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-gpu')

        operation_system = sys.platform

        if operation_system == "win32":
            self.browser = webdriver.Chrome(
                os.getcwd() + "/webdrivers/win/chromedriver.exe", options=opts)
        elif operation_system == "darwin":
            self.browser = webdriver.Chrome(os.getcwd() + "/webdrivers/mac/chromedriver", options=opts)
        elif operation_system == "linux" or operation_system == "linux2":
            self.browser = webdriver.Chrome(os.getcwd() + "/webdrivers/linux/chromedriver", options=opts)
        
        self.Log("Browser started...")

        self.Log("Open Login Page")
        self.browser.get("https://www.instagram.com/accounts/login")

        login_objects = self.WaitForObjects(
            By.CSS_SELECTOR, "input._2hvTZ.pexuQ.zyHYP","Login")
        if login_objects != False:
            login_objects[0].send_keys(self.guiHandle.account_tab.getUsername())
            login_objects[1].send_keys(self.guiHandle.account_tab.getPassword())
            login_objects[1].send_keys(Keys.ENTER)

        time.sleep(3)
        self.loggedIn = True
        self.Log("Logged in...")

        self.guiHandle.account_tab.setLoginStatus()
    def ClickObject(self,mObject):
        try:
            mObject.click()
            return True
        except Exception as error:
            return False
    def FindByCSSAndAttribute(self, mobject, css, attribute):
        try:
            return mobject.find_element_by_css_selector(css).get_attribute(attribute)
        except:
            return False

    def collect_photos_by_hashtag(self, hashtag):
        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        
        for n in range(2,6):
            self.browser.execute_script("window.scrollTo(0, {})".format(n*4000))
            time.sleep(1)

        all_photos = self.WaitForObjects(By.CSS_SELECTOR, "div.v1Nh3.kIKUG._bz0w","CollectPhotos - get Photos")
        if all_photos != False:
            all_links = []
            for photo in all_photos:
                link = self.FindByCSSAndAttribute(photo, 'a', 'href')

                if link != False:
                    all_links.append(link)
            
            commented_photos = self.database.read_all_comments()
            liked_photos = self.database.read_all_likes()
            filtered_links = []
            for link in all_links:
                if link in liked_photos or link in commented_photos:
                    continue
                filtered_links.append(link)

            return filtered_links
        
        return False
    
    def like(self,photo):
        if self.liked_posts_count < self.guiHandle.config.likestoday:
            self.browser.get(photo)

            time.sleep(random.randint(1, 3))

            like_photo = self.WaitForObject(
                By.CSS_SELECTOR, "[aria-label='Gefällt mir']","Like")

            self.Log(f"Like Post: [ {photo} ]")
            if like_photo != False:
                like_photo.click()

                like_photo_check = self.WaitForObject(
                By.CSS_SELECTOR, "[aria-label='Gefällt mir nicht mehr']","Like - Check")
                if like_photo_check != False:
                    self.database.add_like(photo)
                    self.liked_posts_count += 1
                    self.Log(f"Liked Post: [ {photo} ]")

            self.CheckisTempBan()

    def CheckisTempBan(self):
        temp_ban = self.WaitForObjectNoLog(By.CLASS_NAME,"gxNyb")
        if temp_ban != False:
            self.temp_banned = True
            return True
        else:
            return False
    def comments_disabled(self):
        #_7UhW9   xLCgt      MMzan        mDXrS    uL8Hv     l4b0S    
        disabled = self.WaitForObjectNoLog(By.CLASS_NAME,"_7UhW9.xLCgt.MMzan.mDXrS.uL8Hv.l4b0S")
        if disabled != False:
            return True
        else:
            return False

    def write_comment(self, link):
        if self.commented_posts_count < self.guiHandle.config.commentstoday:
            if self.database.find_comment(link) is None:
                self.Log(f"Write comment: {link}")
                self.browser.get(link)
                if self.comments_disabled() == False:
                    commentbox = self.WaitForObject(By.CLASS_NAME, "Ypffh","writeComment-1")
                    if commentbox != False:
                        commentbox.click()
                        commentbox = self.WaitForObject(By.CLASS_NAME, "Ypffh","writeComment-2")
                        if commentbox != False:
                            commentbox.clear()
                            commentbox.send_keys(random.choice(self.database.getComments()))
                            comment_button_x = self.WaitForObjects(By.CLASS_NAME,"sqdOP.yWX7d.y3zKF","writeComment-button")
                            for button in comment_button_x:
                                try:
                                    if button.text == "Posten":
                                            #Kommentar konnte nicht gepostet werden.
                                            button.click()
                                            self.commented_posts_count  += 1
                                            self.database.add_comment(link)
                                            self.Log(f"Comment written.. : [ {link} ]")
                                            break
                                except Exception as error:
                                        with open("errorlog.txt","a") as errorfile:
                                            finalmsg = "Comment click button.. [{}] Message: {}\n".format(datetime.now().strftime("%d-%m-%Y / %H:%M:%S"),error)
                                            errorfile.write(finalmsg)
                                        self.Log("Failed to post comment...")
                else:
                    self.Log("Comments disabled for this post.")     
                self.CheckisTempBan()

    def isProfilePrivate(self):
        try:
            x = self.WaitForObjectNoLog(By.CLASS_NAME,"rkEop")
            if x != False:
                return True
            else:
                return False
        except:
            return False

    def get_Profile(self):
        profile_link = self.WaitForObject(
            By.CLASS_NAME, "sqdOP.yWX7d._8A5w5.ZIAjV","GetProfile - link")
        if profile_link != False:
            return profile_link.get_attribute('href')
        elif profile_link == False:
            return False

    def follow_user(self):
        profile_link = self.get_Profile()
        
        if profile_link != False:
            if self.database.find_following(profile_link) == False:
                self.browser.get(profile_link)
                time.sleep(2)
                self.Log(f"Checking if Profile is private or Public")
                if self.isProfilePrivate() == True:
                    self.Log("Profile is Private, let's Follow.")
                    #fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    
                    follow_private_button = self.WaitForObject(By.CLASS_NAME, "sqdOP.L3NKy.y3zKF","Follow Private - button")

                    if follow_private_button != False:
                        if self.ClickObject(follow_private_button) == True:
                        #follow_private_button.click()  
                            check_private_follow = self.WaitForObject(By.CLASS_NAME, "sqdOP.L3NKy._8A5w5","Check Follow Private - button")
                            if check_private_follow != False:
                                self.followed_count += 1
                                self.Log("Followed Profile...")
                                self.database.add_following(profile_link)
                else:
                    self.Log("Profile is Public, let's Follow.")   
                    follow_public_button = self.WaitForObject(By.CLASS_NAME, "_5f5mN.jIbKX._6VtSN.yZn4P","Follow Public - button")

                    if follow_public_button != False:
                        if self.ClickObject(follow_public_button) == True:
                        #follow_public_button.click()  
                            check_public_follow = self.WaitForObject(By.CLASS_NAME, "fAR91.sqdOP.L3NKy._4pI4F._8A5w5","Check Follow Public - button")
                            if check_public_follow != False:
                                self.followed_count += 1
                                self.Log("Followed Profile...")
                                self.database.add_following(profile_link)
                                

    def unfollow_user(self):
        all_followed_profiles = self.database.get_all_following()
        if all_followed_profiles != None:
            for profile,timestamp_ in all_followed_profiles:
                if self.check_following_time(timestamp_) == True:
                    self.Log("Check if Profile ist still Okay")
                    self.browser.get(profile)
                    time.sleep(3)
                    if ("Diese Seite ist leider nicht verfügbar." in self.browser.page_source):
                        self.database.delete_following(profile)
                        self.Log("Profile is offline, deleting entry...")
                    else:
                        self.Log(f"Unfollowing [ {profile} ] ")
                        unfollow_button_one = self.WaitForObjectNoLog(By.CLASS_NAME,"Igw0E.rBNOH.YBx95._4EzTm")

                        if unfollow_button_one != False:
                            if self.ClickObject(unfollow_button_one) == True:

                                unfollow_button_two = self.WaitForObjectNoLog(By.CLASS_NAME,"aOOlW.-Cab_")
                                if unfollow_button_two != False:
                                    if self.ClickObject(unfollow_button_two) == True:
                                        self.Log("Unfollowed Profile....")
                                        self.unfollowed_counter += 1
                                        self.guiHandle.stats_tab.setUnfollowedStats(self.unfollowed_counter)
                                        self.database.delete_following(profile)

                time.sleep(5)
                                



                    
#bot = MainBot()


            