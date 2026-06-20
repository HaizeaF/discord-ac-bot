import logging
from discord.ext import commands
from bot.scheduler.jobs import start_scheduler

logger = logging.getLogger("discord")

class ReadyEvents(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Radio check")
        synced = await self.bot.tree.sync()
        logger.info(f"Synced {len(synced)} commands.")

        start_scheduler(self.bot)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ReadyEvents(bot))