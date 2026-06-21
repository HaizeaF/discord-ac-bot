import asyncio

from bot.core import webserver
from bot.core.bot import create_bot, load_extensions
from bot.core.config import TOKEN
from bot.core.logger import setup_logger

async def main() -> None:
    """Set up logging, build the bot, load its cogs and start it."""
    setup_logger()

    bot = create_bot()
    await load_extensions(bot)

    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    webserver.keep_alive()
    asyncio.run(main())