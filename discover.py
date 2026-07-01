from modules.league import load_league
from pprint import pprint

league = load_league()

player = league.free_agents(size=1)[0]

print("PLAYER DICTIONARY")
print("=" * 50)
pprint(player.__dict__)
