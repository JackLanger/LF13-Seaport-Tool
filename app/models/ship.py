class Ship:
  
    shipList = []
    def __init__(self, name: str = ""):
        self.__name = name
        self.__capacity = 0
        self.__sailors = 0
        self.shipList.append(self)

    def getName(self) -> str:
        return self.__name

    def getCapacity(self) -> int:
        return self.__capacity

    def getSailor(self) -> int:
        return self.__sailors

    def setName(self, res: str):
        self.__name = res

    def setCapacity(self, res: str):
        self.__capacity = res

    def setSailor(self, amt: int):
        self.__sailors = amt

    def to_dto(self):
        return ShipDTO(
            name=self.__name, capacity=self.__capacity, sailors=self.__sailors
        )

    def update_from_dto(self, ship_dto):
        self.__name = ship_dto.name
        self.__capacity = ship_dto.capacity
        self.__sailors = ship_dto.sailors


class ShipDTO:
    def __init__(
        self, ship_id: int, name: str, capacity: int, sailors: int, level: int = 1
    ):
        self.id = ship_id
        self.name = name
        self.capacity = capacity
        self.sailors = sailors
        self.level = level
