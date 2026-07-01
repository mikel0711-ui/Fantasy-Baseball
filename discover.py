from modules.league import load_league

league = load_league()

player = league.free_agents(size=1)[0]

print("PLAYER ATTRIBUTES")
print("-----------------")

for attr in sorted(dir(player)):
    if attr.startswith("_"):
        continue

    try:
        value = getattr(player, attr)
        print(f"{attr}: {value}")
    except Exception:
        pass
