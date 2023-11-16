from typing import List, Dict, Tuple

from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO


class AlgoResult:
    round_count: int
    rounds: List[Dict[Resource, List[ShipDTO]]]

    def __init__(self, data: List[Tuple[ShipDTO, Resource]] = None):
        self.rounds = []

        for ship, resource in data:
            for i in range(len(self.rounds)):
                if any(ship in ships for ships in self.rounds[i].values()):
                    continue

                if resource.name not in self.rounds[i]:
                    self.rounds[i][resource.name] = [ship]
                    break
                elif ship not in self.rounds[i][resource.name]:
                    self.rounds[i][resource.name].append(ship)
                    break
            else:
                self.rounds.append({resource.name: [ship]})

    def get_round_count(self) -> int:
        return len(self.rounds)

    def add_round(self, round_data):
        self.rounds.append(round_data)

    def print_result(self):
        for n, round_data in enumerate(self.rounds):
            print(f"Round {n + 1}:")
            for resource, ships in round_data.items():
                print(f"  Resource: {resource}")
                for ship in ships:
                    print(f"    Ship Name: {ship.name}, Capacity: {ship.capacity}")
                print("\n")


class Algorithm:
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        self.ships = ships
        self.quest = quest

    def calculate(self) -> [AlgoResult]:
        raise NotImplementedError()
