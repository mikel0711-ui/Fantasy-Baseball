from pathlib import Path
import json
import pandas as pd

from modules import projections


def add_draft_info(record, name, draft_lookup):
    """Add draft and keeper information to a player record."""

    if name in draft_lookup.index:
        draft = draft_lookup.loc[name]

        draft_round = int(draft["Round"])

        record["Draft Round"] = draft_round
        record["Overall Pick"] = int(draft["Overall Pick"])
        record["Original Owner"] = draft["Draft Team"]

        if draft_round == 1:
            record["Keeper Eligible"] = False
            record["Keeper Round"] = None
        else:
            record["Keeper Eligible"] = True
            record["Keeper Round"] = draft_round - 1

    else:
        # Undrafted players
        record["Draft Round"] = None
        record["Overall Pick"] = None
        record["Original Owner"] = None
        record["Keeper Eligible"] = True
        record["Keeper Round"] = "Last"

    return record


def export(folder):
    """
    Build a unified player database.
    """

    folder = Path(folder)

    with open(folder / "league_snapshot.json", "r") as f:
        snapshot = json.load(f)

    free_agents = pd.read_csv(folder / "free_agents.csv")

    projection_df = projections.load()

    projection_df["Player"] = (
        projection_df["Name"]
        .astype(str)
        .str.strip()
    )

    projection_df = projection_df.drop_duplicates("Player")
    projection_lookup = projection_df.set_index("Player")

    draft_df = pd.read_csv(folder / "draft_results.csv")
    draft_lookup = (
        draft_df
        .drop_duplicates("Player")
        .set_index("Player")
    )

    players = []

    # -----------------------------
    # Rostered Players
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
                    if col != "Player":
                        record[col] = proj[col]

            record = add_draft_info(record, name, draft_lookup)

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
                if col != "Player":
                    record[col] = proj[col]

        record = add_draft_info(record, name, draft_lookup)

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
