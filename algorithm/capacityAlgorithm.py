from typing import List, Dict

from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm


class AlgoResult:
    round_count: int
    rounds: [Dict[str, List[ShipDTO]]]


class CapacityAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

    def calculate(self):
        result = AlgoResult()

        if not self.quest.resources:
            result.round_count = 0
            return result

        result.round_count = 1
        result.rounds = [{"Holz": [self.ships]}]

        return result
