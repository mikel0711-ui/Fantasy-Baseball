from modules.league import load_league
from pprint import pprint

league = load_league()

print("=" * 80)
print("SEARCHING FREE AGENTS")
print("=" * 80)

found = False

for player in league.free_agents(size=500):

    if player.name == "Cole Young":

        found = True

        print("\n")
        print("=" * 80)
        print("COLE YOUNG FOUND")
        print("=" * 80)

        pprint(player.__dict__)

        print("\n")
        print("=" * 80)
        print("AVAILABLE ATTRIBUTES")
        print("=" * 80)

        for attr in sorted(dir(player)):
            if not attr.startswith("_"):
                print(attr)

        break

if not found:
    print("\nCole Young is NOT in the top 500 free agents.")
