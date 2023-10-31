from typing import List
from app.models.ship import Ship
from algorithm.questProcessor import Algorithm


class CapacityAlgorithm(Algorithm):
    def calculate(self) -> List[List[List[Ship]]]:
        return [[self.ships]]
