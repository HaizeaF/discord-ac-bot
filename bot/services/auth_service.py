import discord
from bot.core.config import ADMIN_ROLE

def is_admin(member: discord.Member) -> bool:
    """Check whether the member has the admin role."""
    role = discord.utils.get(member.roles, id=ADMIN_ROLE)
    return role is not None