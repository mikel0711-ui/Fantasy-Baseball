from espn_api.baseball import League
import os
from config import LEAGUE_ID, YEAR

def load_league():
    return League(
        league_id=LEAGUE_ID,
        year=YEAR,
        espn_s2=os.environ["ESPN_S2"],
        swid=os.environ["SWID"],
    )
