import math
from typing import List, Dict

from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm


class AlgoResult:
    round_count: int
    rounds: [Dict[str, List[ShipDTO]]]

    def __init__(self):
        self.round_count = 0
        self.rounds = [{}]


class CapacityAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

    @property
    def calculate_rounds(
        self,
    ):
        rounds = []
        total_amount = 0
        for r in self.quest.resources:
            total_amount += r.amount

        def add_ship(ship):
            r.amount -= s.capacity
            ships_used_this_round.append(s)
            current_turn[r.name].append(s)

        while total_amount > 0:
            current_turn = {}
            ships_used_this_round = []
            for r in self.quest.resources:
                current_turn[r.name] = []
                if r.amount == 0:
                    continue
                if len(ships_used_this_round) == len(self.ships):
                    break

                for s in self.ships:
                    if r.amount / s.capacity == 1:
                        add_ship(s)
                        total_amount -= s.capacity
                        break

                for s in self.ships:
                    if s not in ships_used_this_round and r.amount >= s.capacity:
                        add_ship(s)
                        total_amount -= s.capacity
                        if r.amount == 0:
                            break
            if not ships_used_this_round:
                break
            rounds.append(current_turn)

        def find_best_fit_for_excess(new_round, amount):
            sorted_by_capacity = sorted(self.ships, key=lambda x: x.capacity)
            for s in sorted_by_capacity:
                if (new_round and s.capacity >= amount) or (
                    s not in rounds[len(rounds) - 1][r.name]
                ):
                    return s
            return None

        for r in self.quest.resources:
            if r.amount > 0:
                s = find_best_fit_for_excess(False, r.amount)
                s_new_round = find_best_fit_for_excess(True, r.amount)

                if s.capacity < s_new_round.capacity:
                    rounds[len(rounds) - 1][r.name].append(s)
                    r.amount -= s.capacity
                    total_amount -= s.capacity
                else:
                    rounds.append({r.name: [s_new_round]})
                    r.amount -= s_new_round.capacity
                    total_amount -= s_new_round.capacity

        return rounds

    @property
    def calculate(self):
        result = AlgoResult()
        if not self.quest.resources or not self.ships:
            return result
        result.rounds = self.calculate_rounds
        result.round_count = len(result.rounds)
        return result
