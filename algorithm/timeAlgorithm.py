from typing import List, Dict, Tuple
from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm, AlgoResult


class TimeAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

    def calculate(self) -> AlgoResult:
        selected_ships = self.select_ships()
        result = AlgoResult(selected_ships)

        return result

    def select_ships(self):
        selected_ships = []

        for resource in self.quest.resources:
            while resource.amount > 0:
                differences = [
                    (ship, abs(ship.capacity - resource.amount)) for ship in self.ships
                ]
                differences.sort(key=lambda x: x[1])

                if differences:
                    selected_ship, _ = differences[0]
                    resource.amount -= selected_ship.capacity
                    selected_ships.append((selected_ship, resource))

        return selected_ships


if __name__ == "__main__":
    ship1 = ShipDTO(ship_id=1, name="Ship1", capacity=20, sailors=10)
    ship2 = ShipDTO(ship_id=2, name="Ship2", capacity=15, sailors=10)
    ship3 = ShipDTO(ship_id=3, name="Ship3", capacity=25, sailors=10)

    ships = [ship1, ship2, ship3]

    resources = [Resource(name="Wood", amount=30), Resource(name="Fish", amount=50)]

    quest = QuestDTO(id=1, title="Sample Quest", resources=resources)
    time_algo = TimeAlgorithm(ships, quest)
    result = time_algo.calculate()

    result.print_result()


# wenn mehr runden als momentan beste Lösung kann der Algorithmus abgebrochen werden

# rückgabewert anpassen
# multiple ergebnisse durch backtracking (rekursive aufrufe zurücklaufen)
# permutationen set?
