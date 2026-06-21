from dotenv import load_dotenv
import os

load_dotenv()

def _get_env_variable(name: str) -> int:
    """Read a required env variable and cast it to int."""
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Environment variable '{name}' is not set.")
    return int(value)

# Discord token
TOKEN = os.getenv("DISCORD_TOKEN")

# Discord roles
ADMIN_ROLE = _get_env_variable("ADMIN_ROLE_ID")
DRIVER_ROLE = _get_env_variable("DRIVER_ROLE_ID")

# Discord channels
POLL_CHANNEL = _get_env_variable("POLL_CHANNEL_ID")
STANDINGS_CHANNEL = _get_env_variable("STANDINGS_CHANNEL_ID")
RANKING_CHANNEL = _get_env_variable("RANKING_CHANNEL_ID")
COMMAND_CHANNEL = _get_env_variable("COMMANDS_CHANNEL_ID")

# Point system for ranking
POINT_SYSTEM = [1,2,4,6,8,10,12,15,18,25]