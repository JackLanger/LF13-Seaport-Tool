from typing import List
from app.models.quest import Quest
from app.models.ship import Ship


class Algorithm:
    def __init__(self, ships: List[Ship], quest: Quest):
        self.ships = ships
        self.quest = quest

    def calculate(self) -> List[List[Ship]]:
        raise NotImplementedError()


class QuestProcessor:
    def __init__(self, algorithm: Algorithm, ships: List[Ship], quest: Quest):
        self.__algorithm = algorithm
        self.__ships = ships
        self.__quest = quest

    def process_quest(self) -> List[List[Ship]]:
        return self.__algorithm.calculate()
