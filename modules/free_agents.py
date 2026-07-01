import pandas as pd


def export(league, folder):
    """
    Export the top available free agents.
    """

    free_agents = league.free_agents(size=500)

    rows = []

    for player in free_agents:

        try:
            positions = ",".join(player.eligibleSlots)
        except Exception:
            positions = ""

        rows.append({
            "Player": player.name,
            "Position": player.position,
            "Eligible": positions,
            "MLB Team": player.proTeam,
            "Owned %": player.percent_owned,
            "Started %": player.percent_started,
            "Injured": player.injured,
            "Injury": player.injuryStatus,
            "Status": player.status,
        })

    df = pd.DataFrame(rows)

    df = df.sort_values(
        by="Owned %",
        ascending=False
    )

    df.to_csv(
        folder / "free_agents.csv",
        index=False
    )
