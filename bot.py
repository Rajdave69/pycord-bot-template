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
# This is the bot.py file. There should be nothing here except for the code that starts the bot.
# I'd not recommend editing this file, keep it clean and simple. If you want to add more commands, make a new cog.
#
#

import os
import sys
from backend import client, discord_token, log, presence
import discord.utils


# This is what gets run when the bot stars
@client.event
async def on_ready():
    log.info(f"Bot is ready. Logged in as {client.user}")
    await client.change_presence(activity=discord.Game(name=presence))


# Loading all .py files in ./cogs as bot cogs.
# If you don't know what a cog is,
# https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')


# Run the actual bot
try:
    client.run(discord_token)
except discord.LoginFailure:
    log.critical("Invalid Discord Token. Please check your config file.")
    sys.exit()
except Exception as err:
    log.critical(f"Error while connecting to Discord. Error: {err}")
    sys.exit()
