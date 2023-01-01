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
# This is the example.py file. Here is where you'll find the example cog.
# You can use this file as a starting-point for your own cogs.
# This is basically how your cog should be structured. You can add more
# functions to this cog, or you can make a new cog. It's up to you.
#
#

import discord
from discord.ext import commands

# Importing our custom variables/functions from backend.py
from backend import log, embed_template, error_template


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Use @command.Cog.listener() for an event-listener (on_message, on_ready, etc.)
    @commands.Cog.listener()
    async def on_ready(self):
        log.info("Cog: Example.py Loaded")

    # Use @commands.slash_command() for a slash-command
    # I recommend using only slash-commands for your bot.
    @commands.slash_command(name="ping", description="Sends Pong!")
    async def ping(self, ctx):
        # Use `await ctx.respond()` to send a message
        await ctx.respond("pong")

    @commands.slash_command(name="testembed", description="Sends a test embed")
    async def test_embed(self, ctx):
        embed = embed_template
        embed.title = "Test Embed"
        embed.description = "This is a test embed."
        await ctx.respond(embed=embed)

    @commands.slash_command(name="testembed2", description="Sends a test embed")
    async def test_embed2(self, ctx):
        error_embed = error_template("Oops! Something went wrong!")
        await ctx.respond(embed=error_embed)


# The `setup` function is required for the cog to work
# Don't change anything in this function, except for the
# name of the cog (Example) to the name of your class.
def setup(client):
    # Here, `Example` is the name of the class
    client.add_cog(Example(client))
