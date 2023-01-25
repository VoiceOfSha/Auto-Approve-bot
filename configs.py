from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "18466786"))
    API_HASH = getenv("API_HASH", "d2ce12c5c963cbb2210a669def0868aa")
    BOT_TOKEN = getenv("BOT_TOKEN", "5642909631:AAHKzZdDm5eYoFniQfO6IHc7Qqi1OPc9dAA")
    FSUB = getenv("FSUB", "TamilanMoviesChat")
    CHID = int(getenv("CHID", "-1001674828759")
    SUDO = int(getenv("SUDO", "1893496887"))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://AAB:AAB@cluster0.hiuufty.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
