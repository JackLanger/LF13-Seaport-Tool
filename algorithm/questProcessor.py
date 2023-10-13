from app.enums.algorithm_type_enum import AlgorithmType
from typing import List
from app.models.quest import Quest
from app.models.ship import Ship


class Algorithm:
    def calculate(self):
        raise NotImplementedError()

class QuestProcessor:
    def __init__(self, algorithm_type: Algorithm, ships: List[Ship], quest: Quest):
        self.__algorithm_type = algorithm_type
        self.__ships = ships
        self.__quest = quest

    def process_quest(self):
        self.__algorithm_type.calculate()
