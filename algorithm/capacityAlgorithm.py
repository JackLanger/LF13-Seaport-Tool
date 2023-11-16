from typing import List, Tuple
from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm, AlgoResult


class CapacityAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

    @staticmethod
    def add_ships_to_round(ships, quest):
        round_resources = []

        for resource in quest.resources:
            while resource.amount > 0:
                differences = [
                    (ship, abs(ship.capacity - resource.amount)) for ship in ships
                ]
                differences.sort(key=lambda x: x[1])

                selected_ship, _ = (
                    differences[0] if differences else (None, float("inf"))
                )

                if selected_ship:
                    if selected_ship.capacity >= resource.amount:
                        round_resources.append(
                            (selected_ship, Resource(resource.name, resource.amount))
                        )
                        resource.amount = 0
                    else:
                        resource.amount -= selected_ship.capacity
                        round_resources.append(
                            (
                                selected_ship,
                                Resource(resource.name, selected_ship.capacity),
                            )
                        )

        return round_resources

    def calculate(self) -> List[AlgoResult]:
        selected_ships = self.add_ships_to_round(self.ships, self.quest)
        result = [AlgoResult(selected_ships)]
        return result


# if __name__ == "__main__":
#     ship1 = ShipDTO(ship_id=1, name="A", capacity=50, sailors=10)
#     ship2 = ShipDTO(ship_id=2, name="B", capacity=100, sailors=10)
#     ship3 = ShipDTO(ship_id=3, name="C", capacity=200, sailors=10)
#     ship4 = ShipDTO(ship_id=3, name="D", capacity=60, sailors=10)
#
#     ships = [ship1, ship2, ship3, ship4]
#
#     resources = [
#         Resource(name="Wood", amount=400),
#         Resource(name="Fish", amount=150),
#         Resource(name="Stein", amount=200),
#     ]
#
#     quest = QuestDTO(id=1, title="Sample Quest", resources=resources)
#     time_algo = CapacityAlgorithm(ships, quest)
#     result = time_algo.calculate()
#
#     result[0].print_result()
