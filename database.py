import sqlite3
from datetime import datetime

class Datenbank():
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect('datenbank.db')

        self.handle = self.connection.cursor()
    

    def read_all_comments(self):
        self.handle.execute("SELECT url FROM comments")

        list_= [list[0] for list in self.handle.fetchall()]
        return list_
    
    def find_comment(self,url_):
        self.handle.execute("SELECT id,url FROM comments WHERE url=?",(url_,))
        if self.handle.fetchone() != None:
            return True
            
    def delete_comment(self,url_):
        self.handle.execute("DELETE FROM comments WHERE url=?",(url_,))
        self.connection.commit()

    def add_comment(self,url_):
        self.handle.execute("INSERT INTO comments(url) VALUES(?)",(url_,))
        self.connection.commit()


    def read_all_likes(self):
        self.handle.execute("SELECT url FROM likes")
        list_= [list[0] for list in self.handle.fetchall()]
        return list_
    
    def find_like(self,url_):
        self.handle.execute("SELECT id,url FROM likes WHERE url=?",(url_,))
        if self.handle.fetchone() != None:
            return True

    def delete_like(self,url_):
        self.handle.execute("DELETE FROM likes WHERE url=?",(url_,))
        self.connection.commit()

    def add_like(self,url_):
        self.handle.execute("INSERT INTO likes(url) VALUES(?)",(url_,))
        self.connection.commit()


    def find_commentFeed(self,url_):
        self.handle.execute("SELECT id,url FROM commentsFeed WHERE url=?",(url_,))
        if self.handle.fetchone() != None:
            return True
            
    def delete_commentFeed(self,url_):
        self.handle.execute("DELETE FROM commentsFeed WHERE url=?",(url_,))
        self.connection.commit()

    def add_commentFeed(self,url_):
        self.handle.execute("INSERT INTO commentsFeed(url) VALUES(?)",(url_,))
        self.connection.commit()
#datetime.now().strftime("%d-%m-%Y / %H:%M:%S")

    def get_following(self,url_):
        self.handle.execute("SELECT url,timestamp FROM following WHERE url=?",(url_,))
        data = self.handle.fetchone()
        if data != None:
            return data
        else:
            return False

    def find_following(self,url_):
        self.handle.execute("SELECT url,timestamp FROM following WHERE url=?",(url_,))
        if self.handle.fetchone() != None:
            return True
            
    def delete_following(self,url_):
        self.handle.execute("DELETE FROM following WHERE url=?",(url_,))
        self.connection.commit()


    def add_following(self,url_):
        self.handle.execute("INSERT INTO following(url,timestamp) VALUES(?,?)",(url_,datetime.now().strftime("%d-%m-%Y / %H:%M:%S"),))
        self.connection.commit()

    def deleteCommentsToPosts(self):
        self.handle.execute("DELETE FROM settings_comment")
        self.connection.commit()

    def addCommentsToPost(self,comments):
        for comment_ in comments:
            self.handle.execute("INSERT INTO settings_comment(comment) VALUES(?)",(comment_,))
        self.connection.commit()
    
    def getComments(self):
        self.handle.execute("SELECT comment FROM settings_comment")
        list_= [list[0] for list in self.handle.fetchall()]
        return list_   
                
    def deleteHashtag(self):
        self.handle.execute("DELETE FROM settings_hashtag")
        self.connection.commit()

    def addHashtags(self,hashtags):
        for hashtag_ in hashtags:
            self.handle.execute("INSERT INTO settings_hashtag(hashtag) VALUES(?)",(hashtag_,))
        self.connection.commit()
    
    def getHashtags(self):
        self.handle.execute("SELECT hashtag FROM settings_hashtag")
        list_= [list[0] for list in self.handle.fetchall()]
        return list_
        '''data = self.handle.fetchall()
        if data != None:
            data = list(data)
            
            return data
        else:
            return False
        '''

    