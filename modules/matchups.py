import pandas as pd


def export(league, folder):
    """
    Export this week's and next week's matchups. Category stats are
    only meaningful for the current period; next week's row is purely
    for identifying the upcoming opponent ahead of time.
    """

    current_period = league.currentMatchupPeriod
    next_period = current_period + 1

    rows = []

    for period, label in [(current_period, "Current"), (next_period, "Next")]:
        box_scores = league.box_scores(matchup_period=period)

        for box in box_scores:
            row = {
                "Period Type": label,
                "Matchup Period": period,
                "Home Team": box.home_team.team_name,
                "Away Team": box.away_team.team_name if box.away_team else None,
            }

            # Category record/stats only exist for periods that have
            # actually started, but grab them if present either way.
            if label == "Current":
                row["Home Cat Wins"] = box.home_wins
                row["Home Cat Losses"] = box.home_losses
                row["Home Cat Ties"] = box.home_ties
                row["Away Cat Wins"] = box.away_wins
                row["Away Cat Losses"] = box.away_losses
                row["Away Cat Ties"] = box.away_ties
                row["Winner"] = box.winner

            rows.append(row)

    pd.DataFrame(rows).to_csv(
        folder / "matchups.csv",
        index=False
    )
