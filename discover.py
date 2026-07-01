from modules.league import load_league
import inspect

league = load_league()

print(inspect.signature(league.free_agents))
print()
print(league.free_agents.__doc__)
