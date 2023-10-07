from app.enums.algorithm_type_enum import AlgorithmType
from typing import List
from app.models.quest import Quest
from app.models.ship import Ship


class QuestProcessor:
    def __init__(self, algorithm_type: AlgorithmType, ships: List[Ship], quest: Quest):
        self.__algorithm_type = algorithm_type
        self.__ships = ships
        self.__quest = quest

    def get_algorithm_type(self) -> AlgorithmType:
        return self.__algorithm_type

    def get_ships(self) -> List[Ship]:
        return self.__ships

    def get_quest(self) -> Quest:
        return self.__quest

    def process_quest(self) -> None:
        if self.__algorithm_type == AlgorithmType.TIME_CRITICAL:
            self.time_critical_algorithm()
        elif self.__algorithm_type == AlgorithmType.CAPACITY_CRITICAL:
            self.capacity_critical_algorithm()
        else:
            raise ValueError("Invalid algorithm type.")

    def time_critical_algorithm(self):
        pass

    def capacity_critical_algorithm(self):
        pass
