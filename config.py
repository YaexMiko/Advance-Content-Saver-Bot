from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20071888")
    API_HASH = environ.get("API_HASH", "1c4cb9d94b23282abd9ae2a87a521b53")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7716433955:AAFhH0_Y8ltddApzJGLSYbxvNqttwvz-6-8") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Dam:aloksingh@cluster0.6z0hq.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8108281129').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
