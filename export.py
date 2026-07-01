from espn_api.baseball import League
import os
import json
import pandas as pd
from pathlib import Path

EXPORT_DIR = Path("exports")
EXPORT_DIR.mkdir(exist_ok=True)

league = League(
    league_id=23876,
    year=2026,
    espn_s2=os.environ["ESPN_S2"],
    swid=os.environ["SWID"],
)

#################################
# League Settings
#################################

settings = {
    "league_name": league.settings.name,
    "season": 2026,
    "team_count": len(league.teams),
}

with open(EXPORT_DIR / "league_settings.json", "w") as f:
    json.dump(settings, f, indent=2)

#################################
# Standings
#################################

standings = []

for team in league.teams:
    standings.append({
        "team": team.team_name,
        "wins": team.wins,
        "losses": team.losses,
        "ties": team.ties,
    })

pd.DataFrame(standings).to_csv(
    EXPORT_DIR / "standings.csv",
    index=False
)

#################################
# All Rosters
#################################

rosters = []

for team in league.teams:
    for player in team.roster:
        rosters.append({
            "team": team.team_name,
            "player": player.name,
            "positions": ",".join(player.eligibleSlots),
            "injured": player.injuryStatus,
        })

pd.DataFrame(rosters).to_csv(
    EXPORT_DIR / "league_rosters.csv",
    index=False
)

#################################
# My Roster
#################################

my_team = next(
    t for t in league.teams
    if t.team_name == "Jazz Hands"
)

mine = []

for player in my_team.roster:
    mine.append({
        "player": player.name,
        "positions": ",".join(player.eligibleSlots),
        "injury": player.injuryStatus,
    })

pd.DataFrame(mine).to_csv(
    EXPORT_DIR / "my_roster.csv",
    index=False
)

print("Export complete.")
