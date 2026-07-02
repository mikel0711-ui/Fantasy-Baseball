import pandas as pd


def export(league, folder):
    """
    Export current week's matchups (including category-by-category
    results, if available) to matchups.csv
    """

    matchup_period = league.currentMatchupPeriod

    box_scores = league.box_scores(matchup_period=matchup_period)

    rows = []

    for box in box_scores:
        row = {
            "Matchup Period": matchup_period,
            "Home Team": box.home_team.team_name,
            "Away Team": box.away_team.team_name if box.away_team else None,
            "Home Score": getattr(box, "home_score", None),
            "Away Score": getattr(box, "away_score", None),
        }

        # H2H category leagues expose per-category results here.
        # Flatten them into Home_<CAT> / Away_<CAT> / <CAT>_Result columns.
        home_cats = getattr(box, "home_team_cats", None)
        away_cats = getattr(box, "away_team_cats", None)

        if home_cats:
            for cat, detail in home_cats.items():
                row[f"Home_{cat}"] = detail.get("score")
                row[f"{cat}_Result"] = detail.get("result")

        if away_cats:
            for cat, detail in away_cats.items():
                row[f"Away_{cat}"] = detail.get("score")

        rows.append(row)

    pd.DataFrame(rows).to_csv(
        folder / "matchups.csv",
        index=False
    )
