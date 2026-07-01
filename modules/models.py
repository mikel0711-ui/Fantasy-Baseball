from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    positions: list[str] = field(default_factory=list)
    injury: str = ""


@dataclass
class Team:
    name: str
    wins: int
    losses: int
    ties: int
    roster: list[Player] = field(default_factory=list)


@dataclass
class LeagueSnapshot:
    league_name: str
    season: int
    teams: list[Team] = field(default_factory=list)
