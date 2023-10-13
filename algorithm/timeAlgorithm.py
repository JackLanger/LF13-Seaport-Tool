from typing import List

from app.enums.algorithm_type_enum import AlgorithmType
from app.models.quest import Quest
from app.models.ship import Ship
from questProcessor import QuestProcessor, Algorithm


class TimeAlgorithm(Algorithm):
    def __init__(self, algorithm_type: AlgorithmType, ships: List[Ship], quest: Quest):
        super().__init__(algorithm_type, ships, quest)

    def calculate(self):
        print("time")
