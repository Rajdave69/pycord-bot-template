# Python Discord Bot Template

A template for a Discord bot written in Python with the `py-cord` library.

## Features

- Sample config.ini file with comments
- Ready-made base bot (bot.py)
- Customizable config items 
- backend.py for backend functions with the base already set up
- An example cog with a listener and a slash command
- A requirements.txt file with the required libraries needed
- Comments in the code to help you understand what's going on

## How to use

1. Clone the repository
2. Install the required libraries with `pip install -r requirements.txt`
3. Edit the config.ini file with your bot's token and other settings you'd like to change
4. Run the bot with `python bot.py`

## Adding a Cog

Adding a cog is easy. Just create a new file in the `cogs` folder and add the following code:

```py
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, client):
        self.bot = client

def setup(client):
    client.add_cog(MyCog(client))
```

Replace `MyCog` with the name of your cog. Then, add your commands and listeners to the cog.

## Contributing

If you'd like to contribute to this repository, feel free to make a pull request. I'll review it and merge it if it's good.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---