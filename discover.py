from modules.league import load_league

league = load_league()

print("=" * 80)
print("FREE AGENT STATUS COUNTS")
print("=" * 80)

statuses = {}

players = league.free_agents(size=1500)

for player in players:
    status = getattr(player, "status", "UNKNOWN")
    statuses[status] = statuses.get(status, 0) + 1

for status, count in sorted(statuses.items()):
    print(f"{status}: {count}")

print("\n")
print("=" * 80)
print("NON-FREE AGENT PLAYERS")
print("=" * 80)

found = False

for player in players:

    status = getattr(player, "status", "UNKNOWN")

    if status != "FREEAGENT":

        found = True

        print("------------------------------------")
        print(player.name)
        print("Status:", status)

if not found:
    print("No non-free agents returned.")

print("\n")
print("=" * 80)
print("COLE YOUNG SEARCH")
print("=" * 80)

found = False

for player in players:

    if "Cole" in player.name or "Young" in player.name:

        found = True

        print(player.name)
        print("Status:", getattr(player, "status", "UNKNOWN"))

if not found:
    print("Cole Young not returned by free_agents().")
