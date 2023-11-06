from typing import List
from app.models.round import Round
from algorithm.questProcessor import Algorithm
from app.models.solution import Solution


class CapacityAlgorithm(Algorithm):
    def calculate(self) -> List[Solution]:
        resources = self.quest.getResource()
        ships = self.ships

        solutions = []

        for ship in ships:
            r = Round()
            r.addShip((ship, resources[0].name))

            sol = Solution()
            sol.addRound(r)

            solutions.append(sol)

        return solutions
