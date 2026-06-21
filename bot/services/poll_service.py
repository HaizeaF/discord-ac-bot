import discord
from datetime import timedelta

def build_participation_poll() -> discord.Poll:
    """Build the race participation poll with a 7 day timeout."""
    timeout = timedelta(days=7)

    participation_poll = discord.Poll("Participo en la próxima carrera", timeout)
    participation_poll.add_answer(text="Sí", emoji="✅")
    participation_poll.add_answer(text="No", emoji="❌")
    participation_poll.add_answer(text="No sé", emoji="❓")

    return participation_poll