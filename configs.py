# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22672907"))
    API_HASH = getenv("API_HASH", "0ff15ae2153bd8e03b48cb293010bc6a")
    BOT_TOKEN = getenv("BOT_TOKEN", "6615592453:AAEgKfReYuZns7Q-FQVFPITAqWT0q2l6_wU")
    FSUB = getenv("FSUB", "aapna_Movies")
    CHID = int(getenv("CHID", "-1002056115205"))
    SUDO = list(map(int, getenv("SUDO", "6287591671").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rani828719:sVyRWZOrUzIWNfHp@cluster0.zodktob.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
