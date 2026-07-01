from pathlib import Path

from config import EXPORT_DIR
from modules.league import load_league
from modules import standings
from modules import rosters
from modules import owners
from modules import snapshot
from modules import free_agents
from modules import projections
from modules import player_database

folder = Path(EXPORT_DIR)
folder.mkdir(exist_ok=True)

league = load_league()

standings.export(league, folder)
rosters.export(league, folder)
owners.export(league, folder)
snapshot.export(league, folder)
free_agents.export(league, folder)
projections.export(folder)
player.database.export(folder)

print("Export complete.")
