class ShipDTO:
    """

    # Ship Data Transfer Object (DTO)
    Class used to transfer ship data between different consumers.

    - ship_id: int,
    - name: str,
    - capacity: int,
    - sailors: int,
    - level: int = 1
    - storage: List
    """

    def __init__(
        self, ship_id: int, name: str, capacity: int, sailors: int, level: int = 1
    ):
        self.id = ship_id
        self.name = name
        self.capacity = capacity
        self.sailors = sailors
        self.level = level
        self.storage = []

    @property
    def json(self):
        import json

        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "capacity": self.capacity,
                "sailors": self.sailors,
                "level": self.level,
            }
        )
