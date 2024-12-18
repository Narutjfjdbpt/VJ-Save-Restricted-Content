import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24698242"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8d3f1d89c9c59a3de68282a7c9f4d107")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7594799533"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://tuffduffsuff:wXmjFDRrNgALELDo@cluster0.0c6qm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
