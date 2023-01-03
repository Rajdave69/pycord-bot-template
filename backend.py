#   _____  _                       _   ____        _     _______                   _       _
#  |  __ \(_)                     | | |  _ \      | |   |__   __|                 | |     | |
#  | |  | |_ ___  ___ ___  _ __ __| | | |_) | ___ | |_     | | ___ _ __ ___  _ __ | | __ _| |_ ___
#  | |  | | / __|/ __/ _ \| '__/ _` | |  _ < / _ \| __|    | |/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \
#  | |__| | \__ \ (_| (_) | | | (_| | | |_) | (_) | |_     | |  __/ | | | | | |_) | | (_| | ||  __/
#  |_____/|_|___/\___\___/|_|  \__,_| |____/ \___/ \__|    |_|\___|_| |_| |_| .__/|_|\__,_|\__\___|
#                                                                           | |
#                                                                           |_|
#
# Welcome to Raj's Discord Bot Template
#
# This template is designed to be a starting point for your own Discord bot.
# Made by RajDave69 on GitHub.
#
#
# This is the backend.py file. Here is where you'll find all the things which are run on initialization.
# Here you'll find the client, the logger, and the config file's variables.
# If you want to import a global variable or function to multiple cogs, put it here.
# You can also add more variables to the config file and import them here.
#
#

import configparser
import sys
import discord
import logging
from discord.ext import commands
from colorlog import ColoredFormatter

intents = discord.Intents.default()


# Initializing the logger
def colorlogger(name: str = 'my-discord-bot') -> logging.log:
    logger = logging.getLogger(name)
    stream = logging.StreamHandler()

    stream.setFormatter(ColoredFormatter("%(reset)s%(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s"))
    logger.addHandler(stream)
    return logger  # Return the logger


log = colorlogger()

# Loading config.ini
config = configparser.ConfigParser()

try:
    config.read('./data/config.ini')
except Exception as e:
    log.critical("Error reading the config.ini file. Error: " + str(e))
    sys.exit()

# Getting variables from config.ini
try:
    # Getting the variables from `[general]`
    log_level: str = config.get('general', 'log_level')
    presence: str = config.get('general', 'presence')

    # Getting the variables from `[secret]`
    discord_token: str = config.get('secret', 'discord_token')

    # Getting the variables from `[discord]`
    embed_footer: str = config.get('discord', 'embed_footer')
    embed_color: int = int(config.get('discord', 'embed_color'), base=16)
    embed_url: str = config.get('discord', 'embed_url')


except Exception as err:
    log.critical("Error getting variables from the config file. Error: " + str(err))
    sys.exit()

# Set the logger's log level to the one in the config file
if log_level.upper().strip() in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
    log.setLevel(log_level.upper().strip())
else:
    log.setLevel("INFO")
    log.warning(f"Invalid log level `{log_level.upper().strip()}`. Defaulting to INFO.")

# Initializing the client
client = commands.Bot(intents=intents)  # Setting prefix

_embed_template = discord.Embed(
    title="Error!",
    color=embed_color,
    url=embed_url
)
_embed_template.set_footer(text=embed_footer)

embed_template = lambda: _embed_template.copy()


def error_template(description: str) -> discord.Embed:
    _error_template = discord.Embed(
        title="Error!",
        description=description,
        color=0xff0000,
        url=embed_url
    )
    _error_template.set_footer(text=embed_footer)

    return _error_template.copy()

# Add your own functions and variables here
# Happy coding! :D
