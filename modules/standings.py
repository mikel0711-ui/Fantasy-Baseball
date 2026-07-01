import pandas as pd


def export(league, folder):
    """
    Export league standings to standings.csv
    """

    standings = []

    for team in league.teams:
        standings.append({
            "Team": team.team_name,
            "Wins": team.wins,
            "Losses": team.losses,
            "Ties": team.ties,
        })

    pd.DataFrame(standings).to_csv(
        folder / "standings.csv",
        index=False
    )
