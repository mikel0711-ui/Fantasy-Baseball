from modules.league import load_league

league = load_league()

print("League methods:")
for item in dir(league):
    if not item.startswith("_"):
        print(item)
