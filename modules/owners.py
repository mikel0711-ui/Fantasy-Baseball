import pandas as pd

def export(league, folder):

    owners = []

    for team in league.teams:

        owners.append({
            "Team": team.team_name,
            "Owner": getattr(team, "owner", ""),
        })

    pd.DataFrame(owners).to_csv(
        folder / "owners.csv",
        index=False
    )
