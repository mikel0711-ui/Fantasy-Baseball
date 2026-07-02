from config import MY_TEAM
from modules.league import load_league

league = load_league()

my_team = next(t for t in league.teams if t.team_name == MY_TEAM)

print(f"Current matchup period: {league.currentMatchupPeriod}")
print(f"Schedule length: {len(my_team.schedule)}")
print(f"Schedule type: {type(my_team.schedule)}")
print()

for i, opponent in enumerate(my_team.schedule):
    print(f"Index {i}: {opponent}")
