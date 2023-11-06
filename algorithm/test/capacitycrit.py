import unittest

from app.models.quest import Resource
from app.models.ship import ShipDTO


class CapacityAlgorithmTest(unittest.TestCase):
    def one_resource_one_trip(self):
        resources = [Resource("Holz", 1)]
        ships = [ShipDTO(1, "name: str", 1, 1, 1)]

        assert ()


if __name__ == "__main__":
    unittest.main()
