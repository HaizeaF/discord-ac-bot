import logging
import discord
from discord.ext import commands

logger = logging.getLogger("discord")
EXTENSIONS = [
    "bot.commands.track",
    "bot.commands.ranking",
    "bot.commands.polls",
    "bot.commands.moderation",
    "bot.events.ready",
    "bot.events.members"
]

def create_bot() -> commands.Bot:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix="/", intents=intents)

    return bot

async def load_extensions(bot: commands.Bot) -> None:
    for extension in EXTENSIONS:
        try:
            await bot.load_extension(extension)
            logger.info(f"Loaded extension: {extension}")
        except Exception as e:
            logger.exception(f"Failed to load extension {extension}: {e}")
            raise