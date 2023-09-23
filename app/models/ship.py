
class Ship:
    def __init__(self):
        self.__name = ""
        self.__capacity = 0
        self.__sailors = 0

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
