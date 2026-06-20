import logging
import discord
from discord import app_commands
from discord.ext import commands
from bot.core.config import DRIVER_ROLE, RANKING_CHANNEL, STANDINGS_CHANNEL
from bot.services.ranking_service import build_empty_leaderboard, build_results_leaderboard, build_updated_ranking, parse_driver_points
from bot.services.auth_service import is_admin
from bot.core.error_logging import log_app_command_error

NOT_ADMIN_MESSAGE = "No tienes permiso para usar este comando."

class RankingCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
        await log_app_command_error(interaction, error)

    @app_commands.command(name="resultado", description="Publica los resultados de una carrera en el canal de resultados.")
    @app_commands.describe(standings="Pilotos en orden de llegada, separados por coma (usa (DNF) o (DNS) si aplica).", track="Nombre de la pista")
    async def result(self, interaction: discord.Interaction, standings: str, track: str) -> None:
        if not is_admin(interaction.user):
            await interaction.response.send_message(NOT_ADMIN_MESSAGE, ephemeral=True)
            return
        
        standings_channel = self.bot.get_channel(STANDINGS_CHANNEL)

        standings_list = standings.split(",")
        leaderboard = build_results_leaderboard(track, standings_list)

        await standings_channel.send(leaderboard)

        await interaction.response.send_message("Resultado generado", ephemeral=True)

    @app_commands.command(name="reiniciar", description="Publica un ranking vacío en el canal de ranking.")
    async def reset(self, interaction: discord.Interaction) -> None:
        if not is_admin(interaction.user):
            await interaction.response.send_message(NOT_ADMIN_MESSAGE, ephemeral=True)
            return
        
        ranking_channel = self.bot.get_channel(RANKING_CHANNEL)

        driver_role = discord.utils.get(interaction.guild.roles, id=DRIVER_ROLE)
        drivers = [member for member in interaction.guild.members if driver_role in member.roles]

        leaderboard = build_empty_leaderboard([d.display_name for d in drivers])
        await ranking_channel.send(leaderboard)

        await interaction.response.send_message("Ranking reiniciado", ephemeral=True)

    @app_commands.command(name="actualizar", description="Calcula y actualiza el ranking sumando los resultados de las últimas carreras.")
    @app_commands.describe(race_qty="Cantidad de carreras a sumar")
    async def update(self, interaction: discord.Interaction, race_qty: int) -> None:
        if not is_admin(interaction.user):
            await interaction.response.send_message(NOT_ADMIN_MESSAGE, ephemeral=True)
            return
        
        await interaction.response.defer(ephemeral=True)
        
        ranking_channel = self.bot.get_channel(RANKING_CHANNEL)
        standings_channel = self.bot.get_channel(STANDINGS_CHANNEL)

        last_ranking_message = [ranking_message async for ranking_message in ranking_channel.history(limit=1)]
        last_standings_messages = [standings_message.content async for standings_message in standings_channel.history(limit=race_qty)]

        standing_points: dict[str, int] = {}
        for msg_content in last_standings_messages:
            race_points = parse_driver_points(msg_content)

            for driver, pts in race_points.items():
                standing_points[driver] = standing_points.get(driver, 0) + pts

        ranking_points: dict[str, int] = {}
        if last_ranking_message:
            ranking_points = parse_driver_points(last_ranking_message[0].content)

        for driver in standing_points:
            standing_points[driver] += ranking_points.get(driver, 0)

        for driver, pts in ranking_points.items():
            if driver not in standing_points:
                standing_points[driver] = pts

        updated_ranking = build_updated_ranking(standing_points)

        if last_ranking_message:
            await last_ranking_message[0].edit(content=updated_ranking)
        else:
            await ranking_channel.send(updated_ranking)

        await interaction.followup.send("Ranking actualizado", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RankingCommands(bot))