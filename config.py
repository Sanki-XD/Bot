# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23842900"))
API_HASH = os.environ.get("API_HASH", "d21e95895cf2a5b83b0167fdd3b6e541")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5846013903:AAHBWqk4HFLpc9NEMe-b4nAJrGuiJfgfsUk")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5761513990")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Db Name")
DATABASE_URL = os.getenv("DATABASE_URL", "Monfo url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5761513990")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5761513990)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001619097595")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "NixaWorld") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'image') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
