import random
import discord
from discord import app_commands
from discord.ext import commands
from bot.core.error_logging import log_app_command_error

class TrackCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
        await log_app_command_error(interaction, error)

    @app_commands.command(name="pista", description="Genera una pista aleatoria entre los dos números introducidos.")
    @app_commands.describe(start_number="Número inicial del rango", end_number="Número final del rango")
    async def track(self, interaction: discord.Interaction, start_number: int, end_number: int):
        """Pick a random track number within the given range."""
        if start_number > end_number:
            start_number, end_number = end_number, start_number

        result = random.randint(start_number, end_number)
        selected_track = f"```ansi\n\u001b[1;2mPISTA: {result}\n```"
        
        await interaction.response.send_message(selected_track)

async def setup(bot):
    await bot.add_cog(TrackCommands(bot))

