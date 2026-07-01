import pandas as pd


def export(league, folder):

    rows = []

    players = league.free_agents(size=1500)

    for player in players:

        eligible = getattr(player, "eligibleSlots", [])

        rows.append({
            "Player": getattr(player, "name", ""),
            "Status": getattr(player, "status", ""),
            "Owned %": getattr(player, "percent_owned", None),
            "Started %": getattr(player, "percent_started", None),
            "MLB Team": getattr(player, "proTeam", ""),
            "Primary Position": getattr(player, "position", ""),
            "Eligible Positions": ",".join(str(x) for x in eligible),
            "Injury": getattr(player, "injuryStatus", ""),
        })

    df = pd.DataFrame(rows)

    if not df.empty:

        df.sort_values(
            ["Status", "Owned %", "Player"],
            ascending=[True, False, True],
            inplace=True,
        )

    df.to_csv(
        folder / "free_agents.csv",
        index=False,
    )

    print(f"Created free_agents.csv ({len(df)} players)")
