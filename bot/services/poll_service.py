import discord
from datetime import timedelta

def build_participation_poll() -> discord.Poll:
    timeout = timedelta(days=14)

    participation_poll = discord.Poll("Participo en la próxima carrera", timeout)
    participation_poll.add_answer(text="Sí", emoji="✅")
    participation_poll.add_answer(text="No", emoji="❌")
    participation_poll.add_answer(text="No sé", emoji="❓")

    return participation_poll