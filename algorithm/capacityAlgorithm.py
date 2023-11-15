import copy
import math
from typing import List, Tuple
from app.models.quest import QuestDTO, Resource

from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm, AlgoResult


class CapacityAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

        self.__results = []
        self.__bestResult = math.inf
        self.total_resources_needed = 0
        for r in quest.resources:
            self.total_resources_needed += r.amount

    def calculate(self) -> [AlgoResult]:
        self.compute_ships(0, self.quest.resources, [])

        return self.__results

    def compute_ships(
        self,
        resources_shipped: int,
        resources: List[Resource],
        used_ships: List[Tuple[ShipDTO, Resource]],
    ):
        if resources_shipped >= self.total_resources_needed:
            delta = resources_shipped - self.total_resources_needed
            if delta < self.__bestResult:
                self.__results.clear()
                self.__bestResult = delta
                self.__results.append(AlgoResult(used_ships))

            elif delta == self.__bestResult:
                self.__results.append(AlgoResult(used_ships))

            return

        for ship in self.ships:
            for i in range(len(resources)):
                if resources[i].amount > 0:
                    # create a copy of the resources resource for each ship and each resource
                    # in order to compute all the variations
                    res_cpy = copy.deepcopy(resources)
                    res_cpy[i].amount -= ship.capacity
                    self.compute_ships(
                        resources_shipped + ship.capacity,
                        res_cpy,
                        used_ships + [(ship, res_cpy[i])],
                    )
