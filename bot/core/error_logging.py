import logging
import discord
from discord import app_commands

logger = logging.getLogger("discord")

async def log_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
    logger.exception("Error al ejecutar el comando '%s'", interaction.command.name if interaction.command else "desconocido", exc_info=error)