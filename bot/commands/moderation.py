import discord
from discord import app_commands
from discord.ext import commands
from bot.core.config import COMMAND_CHANNEL
from bot.core.error_logging import log_app_command_error

class ModerationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
        await log_app_command_error(interaction, error)

    @app_commands.command(name="borrar", description="Borra las imágenes recientes del canal de comandos.")
    async def delete_images(self, interaction: discord.Interaction) -> None:
        """Delete recent messages containing an image from the commands channel."""
        if interaction.channel_id != COMMAND_CHANNEL:
            await interaction.response.send_message("Este comando solo puede utilizarse en el canal de comandos", ephemeral=True)
            return
        
        await interaction.response.defer(ephemeral=True)
        deleted = 0

        async for message in interaction.channel.history(limit=50):
            for attachment in message.attachments:
                if attachment.content_type and attachment.content_type.startswith("image"):
                    await message.delete()
                    deleted += 1
                    break
            
        await interaction.followup.send(f"{deleted} imágen(es) borradas", ephemeral=True)

async def setup(bot):
    await bot.add_cog(ModerationCommands(bot))