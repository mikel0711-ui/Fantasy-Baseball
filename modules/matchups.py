import pandas as pd

from config import MY_TEAM


def export(league, folder):
    """
    Export current and next week's matchups for MY_TEAM, using each
    team's schedule list. This is reliable for future weeks, unlike
    box_scores(), which only reflects the in-progress matchup period.
    """

    my_team = next(t for t in league.teams if t.team_name == MY_TEAM)

    current_period = league.currentMatchupPeriod
    periods = [
        ("Current", current_period, current_period - 1),
        ("Next", current_period + 1, current_period),
    ]

    rows = []

    for label, period_num, idx in periods:
        if idx < 0 or idx >= len(my_team.schedule):
            continue

        matchup = my_team.schedule[idx]

        if matchup.home_team.team_id == my_team.team_id:
            opponent = matchup.away_team
            my_score = matchup.home_final_score
            opp_score = matchup.away_final_score
        else:
            opponent = matchup.home_team
            my_score = matchup.away_final_score
            opp_score = matchup.home_final_score

        rows.append({
            "Period Type": label,
            "Matchup Period": period_num,
            "Opponent": opponent.team_name,
            "My Score": my_score,
            "Opponent Score": opp_score,
            "Winner": matchup.winner,
        })

    pd.DataFrame(rows).to_csv(
        folder / "matchups.csv",
        index=False
    )
