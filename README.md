# Discord Assetto Corsa Bot
A Discord bot that provides various utilities and management tools for Assetto Corsa tournaments.

## Features
- Posts a weekly poll asking drivers if they will join the next race.
- Records race results and calculates points based on finishing position.
- Maintains a ranking channel, updated by summing points from recent races.
- Picks a random track.
- Lets admins clean up images from the commands channel.
- Renames new members to a 3-letter tag on join.

## Project Structure
```
bot/
├── commands/       # Slash commands (cogs)
├── core/           # Bot setup, config, logging, error handling
├── events/         # Discord event listeners
├── scheduler/      # Scheduled jobs
└── services/       # Business logic
main.py             # Entry point
```

## Setup
### 1. Create a virtual environment and install dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Create a Discord application
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
2. In the **Bot → Privileged Gateway Intents** tab, enable:
   - Server Members Intent
   - Message Content Intent
3. In the **OAuth2 → URL Generator** tab, select `bot` and grant at least the following permissions:
   - Send Messages
   - Manage Messages
   - Manage Nicknames
   - Read Message History
   - Create Polls.
     
   Use the generated URL to invite the bot to your server.
4. Save the token to write it in the `.env` file.

### 3. Get the role and channel IDs
Enable Developer Mode in Discord, then right-click each role/channel and select **Copy ID** for:
- Admin role
- Driver role
- Poll channel
- Standings channel
- Ranking channel
- Commands channel

### 4. Configure environment variables
Copy `.env.example` to `.env` and fill in the values:
 
```bash
cp .env.example .env
```

### 5. Run the bot
```bash
python main.py
```

## Adding New Features
 
### Adding a new command
1. Create a new file in `bot/commands/`, or add a command to an existing file if it fits an existing category.
2. Define a `commands.Cog` subclass with your command as an `@app_commands.command(...)` method.
3.  If the cog is in a new file, add a `cog_app_command_error` handler calling `log_app_command_error`, following the pattern used in the existing cogs, so errors are logged consistently.
4. If the cog is in a new file, register it in the `EXTENSIONS` list in `bot/core/bot.py`.

### Adding a new scheduled job
Add the job to `bot/scheduler/jobs.py`, following the pattern used by `start_scheduler`, and register it with the `scheduler.add_job(...)` call.

### Adding a new event listener
Add a new file in `bot/events/` with a `commands.Cog` using `@commands.Cog.listener()` for the relevant Discord event, and register it in `EXTENSIONS`.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.




