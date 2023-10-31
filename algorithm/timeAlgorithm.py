from typing import List
from app.models.quest import Quest
from app.models.ship import Ship
from algorithm.questProcessor import Algorithm


class TimeAlgorithm(Algorithm):
    def calculate(self) -> List[List[List[Ship]]]:
        return [[self.ships]]
