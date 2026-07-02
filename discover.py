from config import MY_TEAM
from modules.league import load_league

league = load_league()

my_team = next(t for t in league.teams if t.team_name == MY_TEAM)

print("Team-level attributes:")
print([attr for attr in dir(my_team) if not attr.startswith("_")])
