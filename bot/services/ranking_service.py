from datetime import datetime
from bot.services.points_service import generate_points

def build_results_leaderboard(track: str, standings: list[str]) -> str:
    """Build the race results message, assigning points by finishing position."""
    total_drivers = len(standings)
    base_points = generate_points(total_drivers)

    leaderboard = "```ansi\n"
    leaderboard += f"\u001b[1;2m####### 🏁 {track.upper()} 🏁 #######\n"

    for i, driver in enumerate(standings):
        driver = driver.replace(" ", "")
        driver = driver.replace("("," (")

        is_dnx = "(DNF)" in driver.upper() or "(DNS)" in driver.upper()
        pts = 0 if is_dnx else base_points[total_drivers - i - 1]

        leaderboard += (
                f"\u001b[0;31m{i+1}.-\u001b[0m {driver}    "
                f"\u001b[0;32m+{pts} pts\u001b[0m\n"
            )
        
    leaderboard += "\n```"
    return leaderboard
    
def build_empty_leaderboard(driver_names: list[str]) -> str:
    """Build a new ranking message with every driver starting at 0 points."""
    leaderboard = "```ansi\n"
    leaderboard += f"\u001b[1;2m####### 🏆 RANKING {datetime.now().year} 🏆 #######\n"

    for i, name in enumerate(driver_names, 1):
        leaderboard += f"\u001b[0;31m{i}.-\u001b[0m {name}    \u001b[0;32m0 pts\u001b[0m\n"

    leaderboard += "\n```"
    return leaderboard

def parse_driver_points(message: str) -> dict[str, int]:
    """Parse a leaderboard/results message into a {driver: points} dict."""
    driver_points: dict[str, int] = {}

    for line in message.split("\n"):
        if "pts" not in line:
            continue

        clean_line = line.replace(" (DNF)","").replace(" (DNS)","")
        parts = clean_line.split()

        name_part = parts[1]
        points_part = parts[2]
        points_str = points_part.replace("\u001b[0;32m", "").replace("+", "")
        points = int(points_str)

        driver_points[name_part] = driver_points.get(name_part, 0) + points

    return driver_points

def build_updated_ranking(standing_points: dict[str, int]) -> str:
    """Build the ranking message sorted by total points, descending."""
    updated_ranking = "```ansi\n"
    updated_ranking += f"\u001b[1;2m####### 🏆 RANKING {datetime.now().year} 🏆 #######\n"

    sorted_drivers = sorted(standing_points.items(), key=lambda item: item[1], reverse=True)
    for i, (driver, points) in enumerate(sorted_drivers, 1):
        updated_ranking += f"\u001b[0;31m{i}.-\u001b[0m {driver}    \u001b[0;32m{points} pts\u001b[0m\n"

    updated_ranking += "\n```"
    return updated_ranking
