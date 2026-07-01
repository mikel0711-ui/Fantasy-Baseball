import pandas as pd

from modules.league import load_league


def export(folder):
    league = load_league()

    rows = []

    for pick in league.draft:

        rows.append({
            "Pick": pick.round_pick,
            "Round": pick.round_num,
            "Overall Pick": pick.round_pick,
            "Player": pick.playerName,
            "Draft Team": pick.team.team_name
        })

    draft = pd.DataFrame(rows)

    draft.to_csv(
        folder / "draft_results.csv",
        index=False
    )

    print(f"Created draft_results.csv ({len(draft)} picks)")
