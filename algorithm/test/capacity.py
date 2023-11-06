import unittest
from typing import Tuple, Dict, List

from algorithm.capacityAlgorithm import CapacityAlgorithm, AlgoResult
from app.models.quest import Resource, QuestDTO
from app.models.ship import ShipDTO


def get_result(round_count, *rounds: Dict[str, List[ShipDTO]]) -> AlgoResult:
    res = AlgoResult()
    res.round_count = round_count
    res.rounds = [r for r in rounds]

    return res


def get_ship(id, capacity) -> ShipDTO:
    return ShipDTO(id, f"ship-{id}", capacity, 1, 1)


def create_quest(*resources: Resource) -> QuestDTO:
    return QuestDTO(1, "quest", [r for r in resources])


class CapacityAlgorithmTest(unittest.TestCase):
    def assert_equals(self, expected: AlgoResult, result: AlgoResult):
        self.assertTrue(result.round_count == expected.round_count)
        index = 0
        for dict in expected.rounds:
            for k in dict:
                left = result.rounds[index][k]
                right = dict
                self.assertTrue(len(left) == len(right))
            index += 1

    def test_no_resource_no_trips(self):
        ships = [ShipDTO(1, "name: str", 1, 1, 1)]
        quest = create_quest()
        algo = CapacityAlgorithm(ships, quest)
        expected = get_result(0)
        self.assert_equals(expected, algo.calculate)

    def test_one_resource_one_trip(self):
        ships = [ShipDTO(1, "name: str", 1, 1, 1)]
        quest = create_quest(Resource("Holz", 1))
        algo = CapacityAlgorithm(ships, quest)
        expected = get_result(1, {"Holz": ships})
        self.assert_equals(expected, algo.calculate)

    def test_one_resource_two_Trips(self):
        resources = [Resource("Holz", 2)]
        ships = [get_ship(1, 1)]
        quest = QuestDTO(1, "quest", resources)
        algo = CapacityAlgorithm(ships, quest)
        expected = get_result(2, {"Holz": ships}, {"Holz": ships})
        self.assert_equals(expected, algo.calculate)

    def test_two_resource_two_Trips(self):
        resources = [Resource("Holz", 1), Resource("Stein", 1)]
        ships = [get_ship(1, 1)]
        quest = QuestDTO(1, "quest", resources)
        algo = CapacityAlgorithm(ships, quest)
        expected = get_result(2, {"Holz": ships}, {"Stein": ships})
        self.assert_equals(expected, algo.calculate)

    def test_two_resource_one_Trips(self):
        resources = [Resource("Holz", 1), Resource("Stein", 2)]
        ships = [get_ship(1, 1), get_ship(2, 2)]
        quest = QuestDTO(1, "quest", resources)
        algo = CapacityAlgorithm(ships, quest)
        expected = get_result(2, {"Holz": [ships[0]], "Stein": [ships[1]]})
        self.assert_equals(expected, algo.calculate)

    def test_two_resource_two_Trips_with_two_ships(self):
        resources = [Resource("Holz", 3), Resource("Stein", 2)]
        ships = [get_ship(1, 1), get_ship(2, 2)]
        quest = QuestDTO(1, "quest", resources)
        algo = CapacityAlgorithm(ships, quest)
        expected = get_result(
            2, {"Holz": ships, "Stein": [ships[1]]}, {"Stein": [ships[1]]}
        )
        self.assert_equals(expected, algo.calculate)

    def test_two_resource_two_Trips_with_two_ships_non_optimal_condition(self):
        resources = [Resource("Holz", 30), Resource("Stein", 25)]
        ships = [get_ship(1, 10), get_ship(2, 20)]
        quest = QuestDTO(1, "quest", resources)
        algo = CapacityAlgorithm(ships, quest)
        expected = get_result(2, {"Holz": ships}, {"Stein": ships})
        self.assert_equals(expected, algo.calculate)


if __name__ == "__main__":
    unittest.main()
