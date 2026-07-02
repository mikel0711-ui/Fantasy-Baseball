from datetime import date
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
from modules import draft
from modules import matchups

today = date.today().isoformat()  # e.g. "2026-07-02"
folder = Path(EXPORT_DIR) / today
folder.mkdir(parents=True, exist_ok=True)

league = load_league()

print(f"Scoring type: {league.scoring_type}")

standings.export(league, folder)
rosters.export(league, folder)
owners.export(league, folder)
snapshot.export(league, folder)
free_agents.export(league, folder)
projections.export(folder)
draft.export(folder)
player_database.export(folder)
matchups.export(league, folder)

print(f"Export complete: {folder}")
