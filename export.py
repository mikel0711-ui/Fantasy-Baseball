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

from espn_api.baseball.box_score import H2HCategoryBoxScore

today = date.today().isoformat()  # e.g. "2026-07-02"
folder = Path(EXPORT_DIR) / today
folder.mkdir(parents=True, exist_ok=True)

league = load_league()

print(f"Scoring type: {league.scoring_type}")

# The espn_api package only maps 'H2H_CATEGORY' and 'H2H_POINTS' to a
# concrete box score class. ESPN now sends 'H2H_MOST_CATEGORIES' for
# leagues like ours, which the package doesn't recognize, so it falls
# back to an abstract class that can't be instantiated. Force the
# correct class ourselves since H2H_MOST_CATEGORIES behaves the same way.
if league.scoring_type == "H2H_MOST_CATEGORIES":
    league._box_score_class = H2HCategoryBoxScore

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
