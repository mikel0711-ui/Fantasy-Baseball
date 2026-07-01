import pandas as pd
from config import MY_TEAM


def export(league, folder):
    """
    Export all league rosters and your roster.
    """

    all_players = []

    for team in league.teams:
        for player in team.roster:

            try:
                positions = ",".join(player.eligibleSlots)
            except Exception:
                positions = ""

            try:
                injury = player.injuryStatus
            except Exception:
                injury = ""

            all_players.append({
                "Team": team.team_name,
                "Player": player.name,
                "Positions": positions,
                "Injury": injury,
            })

    pd.DataFrame(all_players).to_csv(
        folder / "league_rosters.csv",
        index=False
    )

    my_team = next(
        team for team in league.teams
        if team.team_name == MY_TEAM
    )

    my_players = []

    for player in my_team.roster:

        try:
            positions = ",".join(player.eligibleSlots)
        except Exception:
            positions = ""

        try:
            injury = player.injuryStatus
        except Exception:
            injury = ""

        my_players.append({
            "Player": player.name,
            "Positions": positions,
            "Injury": injury,
        })

    pd.DataFrame(my_players).to_csv(
        folder / "my_roster.csv",
        index=False
    )
