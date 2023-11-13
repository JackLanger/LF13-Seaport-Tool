from typing import List, Dict, Tuple


from flask import json

from app.models.quest import QuestDTO
from app.models.ship import ShipDTO


class AlgoResult:
    round_count: int
    rounds: List[List[Tuple[ShipDTO, str]]]

    def __init__(self, n=0, rounds=None):
        self.round_count = n
        self.rounds = rounds if rounds is not None else []

    def add_round(self, round_data):
        self.rounds.append(round_data)

    def print_result(self):
        print(f"Round Count: {self.round_count}")
        for i, round_data in enumerate(self.rounds):
            print(f"Round {i + 1}:")
            for ship, resource in round_data:
                print(f"  Ship Name: {ship.name}, Capacity: {ship.capacity}, Resource: {resource}")
            print("\n")

class Algorithm:
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        self.ships = ships
        self.quest = quest

    @property
    def calculate(self) -> AlgoResult:
        raise NotImplementedError()


class QuestProcessor:
    def __init__(self, algorithm: Algorithm):
        self.__algorithm = algorithm

    def process_quest(self) -> AlgoResult:
        return self.__algorithm.calculate
