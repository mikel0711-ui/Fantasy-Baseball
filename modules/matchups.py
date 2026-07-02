import pandas as pd


def export(league, folder):
    """
    Export current week's matchups to matchups.csv
    """

    matchup_period = league.currentMatchupPeriod

    box_scores = league.box_scores(matchup_period=matchup_period)

    # TEMP DEBUG: print every attribute on the first box score object
    if box_scores:
        print("Available attributes on box score object:")
        print([attr for attr in dir(box_scores[0]) if not attr.startswith("_")])

    rows = []

    for box in box_scores:
        row = {
            "Matchup Period": matchup_period,
            "Home Team": box.home_team.team_name,
            "Away Team": box.away_team.team_name if box.away_team else None,
        }
        rows.append(row)

    pd.DataFrame(rows).to_csv(
        folder / "matchups.csv",
        index=False
    )
