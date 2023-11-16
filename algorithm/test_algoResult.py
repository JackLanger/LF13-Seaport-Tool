from unittest import TestCase

from algorithm.questProcessor import AlgoResult
from app.models.quest import Resource
from app.models.ship import ShipDTO


class TestAlgoResult(TestCase):
    def test_to_string_empty(self):
        res = AlgoResult()
        self.assertEqual(
            "[]",
            res.to_json(),
        )

    def test_to_string_one_round(self):
        ship_1 = ShipDTO(1, "SHIP_1", 1, 1, 1)
        res_1 = Resource("RES_1", 1)
        self.assertEqual(
            '[{"RES_1":[{"ship_id":1,"name":"SHIP_1", "capacity":1, "sailors":1, "level":1}]},]',
            AlgoResult([(ship_1, res_1)]).to_json(),
        )

    def test_to_string(self):
        ship_1 = ShipDTO(1, "SHIP_1", 1, 1, 1)
        res_1 = Resource("RES_1", 1)
        self.assertEqual(
            '[{"RES_1":[{"ship_id":1,"name":"SHIP_1", "capacity":1, "sailors":1, "level":1}]},{"RES_1":[{"ship_id":1,"name":"SHIP_1", "capacity":1, "sailors":1, "level":1}]},]',
            AlgoResult([(ship_1, res_1), (ship_1, res_1)]).to_json(),
        )

    def test_can_add_twice_same(self):
        ship_1 = ShipDTO(1, "SHIP_1", 1, 1, 1)
        res_1 = Resource("RES_1", 1)
        to_add = [(ship_1, res_1), (ship_1, res_1)]
        result = AlgoResult(to_add)
        expected = [{res_1: [ship_1]}, {res_1: [ship_1]}]

        self.assert_data_equal(expected, result.rounds)

    def test_two_resources_same_ship(self):
        ship_1 = ShipDTO(1, "SHIP_1", 1, 1, 1)
        res_1 = Resource("RES_1", 1)
        res_2 = Resource("RES_2", 1)
        to_add = [(ship_1, res_1), (ship_1, res_2)]
        result = AlgoResult(to_add)
        expected = [{res_1: [ship_1], res_2: [ship_1]}]

        self.assert_data_equal(expected, result.rounds)

    def test_two_resources_two_ships(self):
        ship_1 = ShipDTO(1, "SHIP_1", 1, 1, 1)
        ship_2 = ShipDTO(1, "SHIP_2", 1, 1, 1)
        res_1 = Resource("RES_1", 2)
        res_2 = Resource("RES_2", 1)
        to_add = [(ship_1, res_1), (ship_2, res_1), (ship_1, res_2)]
        result = AlgoResult(to_add)
        expected = [{res_1: [ship_1, ship_2]}, {res_2: [ship_1]}]

        self.assert_data_equal(expected, result.rounds)

    def assert_data_equal(self, expected: [AlgoResult], actual: [AlgoResult]):
        self.assertEqual(len(expected), len(actual))

        for i in range(len(expected)):
            for k in expected[i]:
                for res in expected[i][k]:
                    self.assertEqual(len(res), len(actual[i][k]))
                    for resource in res[i][k]:
                        if resource not in actual[i][k]:
                            self.fail("key %s not found in rounds at index %s" % (k, i))

                        for ship in expected[i][k][resource]:
                            if ship not in actual[i][k][resource]:
                                self.fail(
                                    "ship %s not found in resource %s" % (ship, k)
                                )
