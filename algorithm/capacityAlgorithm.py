import math
from typing import List, Dict

from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm


class AlgoResult:
    round_count: int
    rounds: [Dict[str, List[ShipDTO]]]

    def __init__(self):
        self.round_count = 0
        self.rounds = []


class CapacityAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

    @property
    def calculate(self):
        def calculate_total_capacity(ships: List[ShipDTO]) -> int:
            total_capacity = 0
            for ship in ships:
                total_capacity += ship.capacity
            return total_capacity

        result = AlgoResult()

        ships_total_capacity = calculate_total_capacity(self.ships)

        if not self.quest.resources or ships_total_capacity == 0:
            return result
        # move as much material as possible by utilizing all ships in the quest.
        # Do until the total amount is exhausted or the total capacity exceeds the amount to ship.
        # Repeat for each resource. 0..n rounds where all ships are used to move a single resource.
        for resource in self.quest.resources:
            while resource.amount > 0:
                if resource.amount >= ships_total_capacity:
                    result.rounds.append({resource.name: self.ships})
                    resource.amount -= ships_total_capacity
                else:
                    break

        for i in range(len(self.ships)):
            round = {}
            for resource in self.quest.resources:
                pass

            result.rounds.append(round)

        result.round_count = len(result.rounds)

        return result
