import pandas as pd

from modules.league import load_league


def export(folder):

    league = load_league()

    rows = []

    players = league.free_agents(size=1500)

    for player in players:

        rows.append({
            "Player": player.name,
            "Status": getattr(player, "status", ""),
            "Owned %": getattr(player, "percent_owned", None),
            "Started %": getattr(player, "percent_started", None),
            "MLB Team": getattr(player, "proTeam", ""),
            "Position": getattr(player, "position", ""),
            "Eligible": ",".join(getattr(player, "eligibleSlots", [])),
            "Injury": getattr(player, "injuryStatus", ""),
        })

    df = pd.DataFrame(rows)

    df.sort_values(
        ["Status", "Owned %"],
        ascending=[True, False],
        inplace=True
    )

    df.to_csv(
        folder / "free_agents.csv",
        index=False
    )

    print(f"Created free_agents.csv ({len(df)} players)")
