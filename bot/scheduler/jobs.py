import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.core.config import DRIVER_ROLE, POLL_CHANNEL
from bot.services.poll_service import build_participation_poll

async def _send_poll(bot: discord.Client) -> None:
    """Send the participation poll, mentioning the driver role."""
    channel = bot.get_channel(POLL_CHANNEL)
    role = discord.utils.get(channel.guild.roles, id=DRIVER_ROLE)

    participation_poll = build_participation_poll()
    
    await channel.send(role.mention, poll=participation_poll)

def start_scheduler(bot: discord.Client) -> AsyncIOScheduler:
    """Schedule the poll job to run every Monday."""
    scheduler = AsyncIOScheduler()

    async def _job() -> None:
        await _send_poll(bot)

    scheduler.add_job(_job, 'cron', day_of_week=0)
    scheduler.start()

    return scheduler