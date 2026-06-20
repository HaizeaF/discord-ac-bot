import discord
from discord.ext import commands

class MemberEvents(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        display_name = member.display_name[:3].upper()
        await member.edit(nick=display_name)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MemberEvents(bot))