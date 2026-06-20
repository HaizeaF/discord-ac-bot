import discord
from discord import app_commands
from discord.ext import commands
from bot.core.error_logging import log_app_command_error
from bot.services.poll_service import build_participation_poll
from bot.core.config import DRIVER_ROLE, POLL_CHANNEL

class PollCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
        await log_app_command_error(interaction, error)
        
    @app_commands.command(name="encuesta", description="Envía una encuesta de participación de carrera al canal general.")
    async def poll(self, interaction: discord.Interaction) -> None:
        channel = self.bot.get_channel(POLL_CHANNEL)
        role = discord.utils.get(channel.guild.roles, id=DRIVER_ROLE)

        participation_poll = build_participation_poll()
        await channel.send(role.mention, poll=participation_poll)

        await interaction.response.send_message("Encuesta enviada", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PollCommands(bot))