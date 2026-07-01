from pathlib import Path
import json
import pandas as pd

from modules import projections


def export(folder):
    """
    Build a unified player database from:
      - league_snapshot.json
      - free_agents.csv
      - FanGraphs projections
    """

    folder = Path(folder)

    snapshot = json.load(open(folder / "league_snapshot.json", "r"))

    free_agents = pd.read_csv(folder / "free_agents.csv")

    projection_df = projections.load()

    # -----------------------------
    # Normalize projection names
    # -----------------------------
    projection_df["Player"] = (
        projection_df["Name"]
        .astype(str)
        .str.strip()
    )

    projection_df = projection_df.drop_duplicates("Player")

    projection_lookup = projection_df.set_index("Player")

    players = []

    # -----------------------------
    # Rostered players
    # -----------------------------
    for team in snapshot["teams"]:

        owner = team["team"]

        for player in team["roster"]:

            name = player["name"]

            record = {
                "Player": name,
                "Owner": owner,
                "On My Team": owner == "Shitty Mike",
                "Free Agent": False,
                "Owned %": 100,
                "Started %": None,
                "MLB Team": None,
                "Primary Position": None,
                "Eligible Positions": ",".join(player.get("positions", [])),
                "Injury": player.get("injury", ""),
            }

            if name in projection_lookup.index:

                proj = projection_lookup.loc[name]

                for col in projection_df.columns:
                    if col == "Player":
                        continue
                    record[col] = proj[col]

            players.append(record)

    # -----------------------------
    # Free Agents
    # -----------------------------
    rostered = {p["Player"] for p in players}

    for _, fa in free_agents.iterrows():

        name = fa["Player"]

        if name in rostered:
            continue

        record = {
            "Player": name,
            "Owner": "",
            "On My Team": False,
            "Free Agent": True,
            "Owned %": fa.get("Owned %"),
            "Started %": fa.get("Started %"),
            "MLB Team": fa.get("MLB Team"),
            "Primary Position": fa.get("Position"),
            "Eligible Positions": fa.get("Eligible"),
            "Injury": fa.get("Injury"),
        }

        if name in projection_lookup.index:

            proj = projection_lookup.loc[name]

            for col in projection_df.columns:
                if col == "Player":
                    continue
                record[col] = proj[col]

        players.append(record)

    database = pd.DataFrame(players)

    database.sort_values(
        ["Free Agent", "Player"],
        ascending=[True, True],
        inplace=True
    )

    database.to_csv(
        folder / "player_database.csv",
        index=False
    )

    print(f"Created player_database.csv ({len(database)} players)")
