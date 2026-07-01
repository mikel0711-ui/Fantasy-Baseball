from modules.league import load_league
from pprint import pprint

league = load_league()

# Find your team
for team in league.teams:
    if team.team_name == "Shitty Mike":

        print("=" * 80)
        print("TEAM ATTRIBUTES")
        print("=" * 80)

        pprint(team.__dict__)

        print("\n")
        print("=" * 80)
        print("ROSTER")
        print("=" * 80)

        for player in team.roster:
            print(player.name)

        break
