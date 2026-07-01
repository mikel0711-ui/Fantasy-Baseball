from pathlib import Path

from config import EXPORT_DIR
from modules.league import load_league
from modules import standings
from modules import rosters
from modules import owners

folder = Path(EXPORT_DIR)
folder.mkdir(exist_ok=True)

league = load_league()

standings.export(league, folder)
rosters.export(league, folder)
owners.export(league, folder)

print("Export complete.")
