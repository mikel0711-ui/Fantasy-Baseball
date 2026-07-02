from config import MY_TEAM
from modules.league import load_league

league = load_league()

my_team = next(t for t in league.teams if t.team_name == MY_TEAM)

next_matchup = my_team.schedule[league.currentMatchupPeriod]  # index = next period - 1

print("Matchup-level attributes:")
print([attr for attr in dir(next_matchup) if not attr.startswith("_")])
