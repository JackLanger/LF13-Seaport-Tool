class Quest:
    def __init__(self):
        self.__resource = ""
        self.__amount = 0

    def getResource(self) -> str:
        return self.__resource

    def getAmount(self) -> int:
        return self.__amount

    def setResource(self, res: str):
        self.__resource = res

    def setAmount(self, amt: int):
        self.__amount = amt
