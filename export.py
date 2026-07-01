from espn_api.baseball import League
import os

league = League(
    league_id=23876,
    year=2026,
    espn_s2=os.environ["ESPN_S2"],
    swid=os.environ["SWID"]
)

my_team = league.teams[0]

print(f"League: {league.settings.name}")
print(f"My team: {my_team.team_name}")

for player in my_team.roster:
    print(player.name)
