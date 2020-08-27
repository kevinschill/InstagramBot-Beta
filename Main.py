from MainBot import MainBot
from GUI import MainGui
import threading
import time, random

from tkinter.font import Font


bot = MainBot()

gui = MainGui(bot)

def MainLoop():

    bot.setupDatabase()

    while True:
        time.sleep(0.1)
        if bot.loggedIn == True:
            if bot.bot_running == True:
                if gui.settings_tab.like_settings.getLikeStatus() == True or gui.settings_tab.comment_settings.getCommentStatus() == True:
                    collected_photos = bot.collect_photos_by_hashtag(random.choice(bot.database.getHashtags()))

                    if collected_photos != False:

                        for post in collected_photos:
                            if bot.bot_running == True:
                                if bot.temp_banned == False:
                                    if gui.settings_tab.like_settings.getLikeStatus() == True:
                                        bot.like(post)

                                        bot.guiHandle.stats_tab.setLikedStats(bot.liked_posts_count)

                                        sleep_from,sleep_to = gui.settings_tab.like_settings.getLikeSleepReal()
                                        time.sleep(random.randint(sleep_from,sleep_to))
                                        
                                    
                                    if gui.settings_tab.comment_settings.getCommentStatus() == True:
                                        bot.write_comment(post)

                                        bot.guiHandle.stats_tab.setCommentsStats(bot.commented_posts_count)

                                        sleep_from,sleep_to = gui.settings_tab.comment_settings.getCommentSleepReal()
                                        time.sleep(random.randint(sleep_from,sleep_to))
                                    
                                    if gui.settings_tab.follow_settings.getFollowStatus() == True:
                                        bot.follow_user()
                                        
                                        bot.guiHandle.stats_tab.setFollowedStats(bot.followed_count)

                                        sleep_from,sleep_to = gui.settings_tab.follow_settings.getFollowSleepReal()
                                        time.sleep(random.randint(sleep_from,sleep_to))

                                elif bot.temp_banned == True:
                                    gui.temp_ban_text.configure(text="Temp Ban: True, waiting 10 Minutes",font=Font(family="Consolas", size=14, weight="normal"))
                                    gui.temp_ban_text.place(x=80,y=280)
                                    gui.log_tab.writeLog("We are Temp Banned... wait 10 Minutes....")
                                    time.sleep(600)
                                    bot.temp_banned = False
                                    gui.temp_ban_text.configure(text="Temp Ban: False",font=Font(family="Consolas", size=11, weight="normal"))
                                    gui.temp_ban_text.place(x=150,y=280)
                if gui.settings_tab.unfollow_settings.getUnfollowStatus() == True:
                    if bot.temp_banned == False:
                        bot.unfollow_user()

bot_loop_thread = threading.Thread(target=MainLoop)

bot_loop_thread.start()


gui.start_gui()