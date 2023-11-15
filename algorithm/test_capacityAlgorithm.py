from typing import List, Dict
from unittest import TestCase

from algorithm.capacityAlgorithm import CapacityAlgorithm
from algorithm.questProcessor import AlgoResult
from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO


class TestCapacityAlgorithm(TestCase):
    def test_calculate_with_single_round(self):
        ship_1 = ShipDTO(1, "SHIP_1", 1, 1, 1)
        res_1 = Resource("RES_1", 1)
        quest = QuestDTO(1, "quest", [res_1])
        algo = CapacityAlgorithm([ship_1], quest)
        result = algo.calculate()
        expected = [AlgoResult([(ship_1, res_1)])]
        self.assert_data_equal(expected, result)

    def test_calculate_with_two_rounds(self):
        ship_1 = ShipDTO(1, "SHIP_1", 1, 1, 1)
        res_1 = Resource("RES_1", 2)
        quest = QuestDTO(1, "quest", [res_1])
        algo = CapacityAlgorithm([ship_1], quest)
        result = algo.calculate()
        expected = [AlgoResult([(ship_1, res_1), (ship_1, res_1)])]
        self.assert_data_equal(expected, result)

    def test_calculate_with_two_rounds_tow_ships(self):
        ship_1 = ShipDTO(1, "SHIP_1", 1, 1, 1)
        ship_2 = ShipDTO(1, "SHIP_2", 2, 1, 1)
        res_1 = Resource("RES_1", 2)
        quest = QuestDTO(1, "quest", [res_1])
        algo = CapacityAlgorithm([ship_1, ship_2], quest)
        result = algo.calculate()
        expected = [
            AlgoResult([(ship_1, res_1), (ship_1, res_1)]),
            AlgoResult([(ship_2, res_1)]),
        ]
        self.assert_data_equal(expected, result)

    def assert_data_equal(self, expected, actual):
        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            expected_algo_result = expected[i]
            actual_algo_result = actual[i]

            for j in range(len(expected_algo_result.rounds)):
                expected_dict = expected_algo_result.rounds[j]
                actual_dict = actual_algo_result.rounds[j]
                for key in expected_dict:
                    if key not in actual_dict:
                        self.fail(
                            "key: [%s] not found in actual_dict: [%s]"
                            % (key, actual_dict)
                        )

                    for expected_ship in expected_dict[key]:
                        if expected_ship not in actual_dict[key]:
                            self.fail("Ship [%s] missing in actual")
