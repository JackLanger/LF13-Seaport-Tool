from typing import List


from app.models.quest import QuestDTO
from app.models.ship import ShipDTO
from questProcessor import Algorithm


class Round:
    ships: List[ShipDTO] = []


class AlgoResult:
    rounds = []


class CapacityAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(self, ships, quest)

    def calculate(self) -> AlgoResult:
        print("capacity")
