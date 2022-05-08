import os
from os.path import dirname, join

from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")
# BOT_ID = int(os.environ.get("BOT_ID"))
GUILD_ID = int(os.environ.get("GUILD_ID"))
APPLICATION_ID = int(os.environ.get("APPLICATION_ID"))
