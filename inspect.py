from espn_api.baseball import League
import os
import json

league = League(
    league_id=23876,
    year=2026,
    espn_s2=os.environ["ESPN_S2"],
    swid=os.environ["SWID"],
)

team = league.teams[0]
player = team.roster[0]

def serialize(obj):
    output = {}

    for name in dir(obj):
        if name.startswith("_"):
            continue

        try:
            value = getattr(obj, name)

            if callable(value):
                continue

            output[name] = str(value)

        except Exception:
            pass

    return output

with open("exports/league_object.json", "w") as f:
    json.dump(serialize(league), f, indent=2)

with open("exports/team_object.json", "w") as f:
    json.dump(serialize(team), f, indent=2)

with open("exports/player_object.json", "w") as f:
    json.dump(serialize(player), f, indent=2)

print("Inspection complete.")
