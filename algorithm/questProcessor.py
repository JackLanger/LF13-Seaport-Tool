from typing import List, Dict, Tuple


from flask import json

from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO


class AlgoResult:
    round_count: int
    rounds: List[Dict[Resource, List[ShipDTO]]]

    def __init__(self, data: List[Tuple[ShipDTO, Resource]] = None):
        self.rounds = []
        for ship, resource in data:
            if len(self.rounds) == 0:
                self.rounds.append({resource.name: [ship]})
                continue

            ship_added = False
            for i in range(len(self.rounds)):
                if resource.name not in self.rounds[i]:
                    self.rounds[i][resource.name] = [ship]
                    ship_added = True
                elif ship not in self.rounds[i][resource.name]:
                    self.rounds[i][resource.name].append(ship)

            if not ship_added:
                self.rounds.append({resource.name: [ship]})

    def add_round(self, round_data):
        self.rounds.append(round_data)

    def print_result(self):
        print(f"Round Count: {self.round_count}")
        for i, round_data in enumerate(self.rounds):
            print(f"Round {i + 1}:")
            for ship, resource in round_data:
                print(
                    f"  Ship Name: {ship.name}, Capacity: {ship.capacity}, Resource: {resource}"
                )
            print("\n")


class Algorithm:
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        self.ships = ships
        self.quest = quest

    def calculate(self) -> AlgoResult:
        raise NotImplementedError()
