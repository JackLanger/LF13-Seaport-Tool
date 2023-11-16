from typing import List, Dict, Tuple
from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm, AlgoResult


class TimeAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)
        self.original_ships = list(ships)

    def calculate(self) -> [AlgoResult]:
        selected_ships = self.select_ships()
        result = [AlgoResult(selected_ships)]

        return result

    def select_ships(self):
        all_rounds = []
        remaining_resources = list(self.quest.resources)

        while remaining_resources and self.ships:
            current_round = []

            for ship in self.ships:
                differences = [
                    (resource, abs(ship.capacity - resource.amount))
                    for resource in remaining_resources
                ]
                differences.sort(key=lambda x: x[1])

                if differences:
                    selected_resource, _ = differences[0]
                    selected_resource.amount -= ship.capacity
                    current_round.append((ship, selected_resource))

                    if selected_resource.amount <= 0:
                        remaining_resources.remove(selected_resource)

            all_rounds.append(current_round)

        selected_ships = [item for sublist in all_rounds for item in sublist]

        return selected_ships


if __name__ == "__main__":
    ship1 = ShipDTO(ship_id=1, name="A", capacity=50, sailors=10)
    ship2 = ShipDTO(ship_id=2, name="B", capacity=100, sailors=10)
    ship3 = ShipDTO(ship_id=3, name="C", capacity=200, sailors=10)
    ship4 = ShipDTO(ship_id=3, name="D", capacity=60, sailors=10)

    ships = [ship1, ship2, ship3, ship4]

    resources = [
        Resource(name="Wood", amount=400),
        Resource(name="Fish", amount=150),
        Resource(name="Stein", amount=200),
    ]

    quest = QuestDTO(id=1, title="Sample Quest", resources=resources)
    time_algo = TimeAlgorithm(ships, quest)
    result = time_algo.calculate()

    result[0].print_result()
