# FILL THESE VALUES ACCORDINGLY.

from RomeoBot.config.hell_config import Config

class Development(Config):
  # get these values from my.telegram.org. 
  APP_ID = 18551764    # 9 is a placeholder. Fill your 6 digit api id
  API_HASH = "991a66d509729ab73929bb42b514dce5"   # replace this with your api hash

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://lwftbwjfvfhqce:65f091612658e9ca1cb2362fc5f436519d55f2f0bac09afe5b140147772aa4d8@ec2-54-86-106-48.compute-1.amazonaws.com:5432/d2t6slnsdhqikq"
  ALIVE_NAME = "Romeo"
  # After cloning the repo and installing requirements...
  # Do `python string.py` and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  ROMEOBOT_SESSION = "1BVtsOJIBu6l-XVj70_qR-j1FjzNVWyZr3r-CSE-Eo-nBJmTCifjYCZJh6vrrWK2Qyr0ILnSW_A6KSy5BMKL82aI-5MiNFVrZ0bn_4aoOIVPghIBLMMsqBNWVpfEpCsV25tekhpTa5oMmWiYd7ATq-jHqRzvH89XALr7Y7RGO3xIINYctMhnYA3oPavStkihMxEp7P3fZ7649GjUbAS_SiyLGryovxQMoNinChRn1ZcVi4MnYdxXOI2yvNScgufg9G2qRg_XU3FjxcIh4t_4yI0MyLtim4knoGirDL47F1ZFtYTyX2qLV6UeWH7bpva1vF7pEjOSGMo2CLxo8YoYYE4xmz-5HVKE="

  # Create a bot in @BotFather
  # And fill the following values with bot token and username.
  BOT_TOKEN = "5604091752:AAEbdcctzFVW_eET0jWCbA8IYl7OEoOnHos" #token
  #FILL BOT USERNAME WITHOUT @
  BOT_USERNAME = "Uff_ye_Adaaaabot"
  # Custom Command Handler. 
  HANDLER = "."
 

  # Custom Command Handler for sudo users.
  SUDO_HANDLER = "."
  # if u want to add sudo then remove #
  #SUDO_USERS = []


# end of required config
# bot
