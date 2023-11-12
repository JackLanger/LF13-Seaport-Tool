from typing import List
from app.models.quest import QuestDTO
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm, AlgoResult


class CapacityAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

    @staticmethod
    def create_new_round(ships, quest, result):
        new_round = []
        used_ships = set()

        round_resources = []

        for resource in quest.resources:
            if resource.amount > 0:
                differences = [
                    (ship, abs(ship.capacity - resource.amount))
                    for ship in ships
                    if ship not in used_ships
                ]
                differences.sort(key=lambda x: x[1])

                selected_ship, _ = (
                    differences[0] if differences else (None, float("inf"))
                )

                if selected_ship:
                    if selected_ship.capacity == resource.amount:
                        used_ships.add(selected_ship)
                        resource.amount = 0
                        round_resources.append((selected_ship, resource.name))
                    else:
                        used_ships.add(selected_ship)
                        resource.amount -= selected_ship.capacity
                        round_resources.append((selected_ship, resource.name))

        new_round.extend(round_resources)

        if new_round:
            result.append(new_round)

    def calculate(self) -> AlgoResult:
        result = []

        while any(resource.amount > 0 for resource in self.quest.resources):
            self.create_new_round(self.ships, self.quest, result)

        result = AlgoResult(len(result), result)
        return result


# if __name__ == "__main__":
#     ship1 = ShipDTO(ship_id=1, name="Ship1", capacity=20, sailors=10)
#     ship2 = ShipDTO(ship_id=2, name="Ship2", capacity=15, sailors=10)
#     ship3 = ShipDTO(ship_id=3, name="Ship3", capacity=25, sailors=10)
#
#     ships = [ship1, ship2, ship3]
#
#     resources = [Resource(name="Wood", amount=30), Resource(name="Fish", amount=50)]
#
#     quest = QuestDTO(id=1, title="Sample Quest", resources=resources)
#     time_algo = CapacityAlgorithm(ships, quest)
#     result = time_algo.calculate()
#
#     result.print_result()
