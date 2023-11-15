from typing import List
from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm, AlgoResult


class TimeAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

    def calculate(self) -> AlgoResult:
        all_solutions = []
        resutls = []

        while any(resource.amount > 0 for resource in self.quest.resources):
            new_round = self.create_new_round()
            if new_round:
                resutls.append(new_round)

        all_solutions.append(resutls)
        filtered_solutions = self.filter_solutions(all_solutions)

        result = AlgoResult(len(filtered_solutions), filtered_solutions)
        return result

    def create_new_round(self):
        new_round = []
        used_ships = set()

        while any(resource.amount > 0 for resource in self.quest.resources):
            round_resources = []

            for resource in self.quest.resources:
                if resource.amount > 0:
                    differences = [
                        (ship, abs(ship.capacity - resource.amount))
                        for ship in self.ships
                        if ship not in used_ships
                    ]
                    differences.sort(key=lambda x: x[1])

                    if differences:
                        selected_ship, _ = differences[0]
                        used_ships.add(selected_ship)
                        resource.amount -= selected_ship.capacity
                        round_resources.append((selected_ship, resource.name))

            if not round_resources:
                break

            new_round.extend(round_resources)

        return new_round

    def filter_solutions(self, all_solutions):
        if not all_solutions:
            return []

        # Sort solutions based on criteria
        all_solutions.sort(
            key=lambda solution: (
                len(solution),
                sum(int(d[1]) for ship, d in solution[0] if isinstance(d[1], int)),
            )
        )

        min_rounds = len(all_solutions[0])

        min_round_solutions = [
            solution for solution in all_solutions if len(solution) == min_rounds
        ]

        return min_round_solutions


# Example usage
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
