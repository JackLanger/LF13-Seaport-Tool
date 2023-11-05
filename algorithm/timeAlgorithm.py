from typing import List
from app.models.round import Round
from algorithm.questProcessor import Algorithm
from app.models.solution import Solution


class TimeAlgorithm(Algorithm):
    def calculate(self) -> List[Solution]:
        resources = self.quest.getResource()
        ships = self.ships

        r = Round()
        r.addShip((ships[0], resources[0]))

        sol = Solution()
        sol.addRound(r)

        return [sol]
