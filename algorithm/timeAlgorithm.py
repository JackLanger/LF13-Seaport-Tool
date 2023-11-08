from typing import List

from app.models.quest import QuestDTO
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm


class TimeAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

    def calculate(self):
        total_amount = 0
        total_capacity = 0

        for r in self.quest.resources:
            total_amount += r.amount

        for s in self.ships:
            total_capacity += s.capacity

        result = []
        used_ships = []
        current = {}
        ships_by_capacity = sorted(self.ships, key=lambda x: x.capacity, reverse=True)

        while total_amount > 0:
            for r in self.quest.resources:
                if r.amount > 0 and total_capacity <= r.amount:
                    result.append({r.name: self.ships})
                    total_amount -= r.amount
                    r.amount -= total_capacity

                else:
                    current[r.name] = []

                    for s in ships_by_capacity:
                        if s not in used_ships:
                            used_ships.append(s)
                            r.amount -= s.capacity
                            current[r.name].append(s)

                        if r.amount <= 0:
                            break

        result.append(current)
        return result
