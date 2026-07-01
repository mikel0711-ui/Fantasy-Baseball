from pathlib import Path
import pandas as pd


def load(folder=None):
    """
    Load hitter and pitcher projection files into one DataFrame.
    """

    if folder is None:
        folder = Path("data/projections")

    hitters = pd.read_csv(folder / "hitters.csv")
    hitters["PlayerType"] = "Hitter"

    pitchers = pd.read_csv(folder / "pitchers.csv")
    pitchers["PlayerType"] = "Pitcher"

    projections = pd.concat(
        [hitters, pitchers],
        ignore_index=True
    )

    projections.columns = [
        str(col).strip() for col in projections.columns
    ]

    return projections


def export(folder):
    """
    Export the combined projection database.
    """

    projections = load()

    projections.to_csv(
        folder / "player_projections.csv",
        index=False
    )
