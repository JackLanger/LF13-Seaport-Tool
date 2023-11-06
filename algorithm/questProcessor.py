from typing import List
from app.models.quest import QuestDTO
from app.models.ship import ShipDTO


class Algorithm:
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        self.ships = ships
        self.quest = quest

    def calculate(self):
        raise NotImplementedError()


class QuestProcessor:
    def __init__(self, algorithm: Algorithm, ships: List[ShipDTO], quest: QuestDTO):
        self.__algorithm = algorithm
        self.__ships = ships
        self.__quest = quest

    def process_quest(self):
        self.__algorithm.calculate()
