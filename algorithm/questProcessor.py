from typing import List, Dict

from flask import json

from app.models.quest import QuestDTO
from app.models.ship import ShipDTO


class AlgoResult:
    round_count: int
    rounds: [Dict[str, List[ShipDTO]]]

    def __init__(self, n=0, rounds=[{}]):
        self.round_count = n
        self.rounds = rounds

    @property
    def json(self):
        _rounds = []
        for r in self.rounds:
            _rounds.append(r)
            for k in r:
                for s in r[k]:
                    s = s.json

        return json.dumps({"round_count": self.round_count, "rounds": _rounds})


class Algorithm:
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        self.ships = ships
        self.quest = quest

    @property
    def calculate(self) -> AlgoResult:
        raise NotImplementedError()


class QuestProcessor:
    def __init__(self, algorithm: Algorithm):
        self.__algorithm = algorithm

    def process_quest(self) -> AlgoResult:
        return self.__algorithm.calculate
