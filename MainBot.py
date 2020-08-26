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

    def check_following_time(self,url_):
        u,ti = self.database.get_following(url_)
        followed_time = datetime.strptime(ti, "%d-%m-%Y / %H:%M:%S")
        time_now = datetime.strptime(datetime.now().strftime("%d-%m-%Y / %H:%M:%S"), "%d-%m-%Y / %H:%M:%S")

        td_mins = int(round(abs((followed_time - time_now).total_seconds()) / 60))

        if td_mins >= 60: # 1 Std
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

    def write_comment(self, link):
        if self.commented_posts_count < self.guiHandle.config.commentstoday:
            if self.database.find_comment(link) is None:
                self.Log(f"Write comment: {link}")
                self.browser.get(link)
            
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
                self.CheckisTempBan()
                    
#bot = MainBot()


            