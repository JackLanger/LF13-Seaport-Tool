from app.enums.algorithm_type_enum import AlgorithmType
from typing import List
from app.models.quest import Quest
from app.models.ship import Ship


class QuestProcessor:
    def __init__(self, algorithm_type: AlgorithmType, ships: List[Ship], quest: Quest):
        self.__algorithm_type = algorithm_type
        self.__ships = ships
        self.__quest = quest

    def process_quest(self):
        if self.__algorithm_type == AlgorithmType.TIME_CRITICAL:
            return self.time_critical_algorithm()
        elif self.__algorithm_type == AlgorithmType.CAPACITY_CRITICAL:
            return self.capacity_critical_algorithm()
        else:
            raise ValueError("Invalid algorithm type.")

    def time_critical_algorithm(self):
        pass

    def capacity_critical_algorithm(self):
        pass
