import json


def export(league, folder):

    snapshot = {
        "league": {
            "name": league.settings.name,
            "teams": len(league.teams),
        },
        "standings": [],
        "teams": []
    }

    for team in league.teams:

        snapshot["standings"].append({
            "team": team.team_name,
            "wins": team.wins,
            "losses": team.losses,
            "ties": team.ties,
        })

        roster = []

        for player in team.roster:

            try:
                positions = player.eligibleSlots
            except Exception:
                positions = []

            try:
                injury = player.injuryStatus
            except Exception:
                injury = ""

            roster.append({
                "name": player.name,
                "positions": positions,
                "injury": injury,
            })

        snapshot["teams"].append({
            "team": team.team_name,
            "roster": roster,
        })

    with open(folder / "league_snapshot.json", "w") as f:
        json.dump(snapshot, f, indent=2)
