from importlib import resources
from typing import List


class Resource:
    def __init__(self, name: str, amount: int = 0):
        self.name = name
        self.amount: int = 0


class Quest:
    def __init__(self, title: str = ""):
        self.__title = title
        self.__resources = []
        self.__amount = 0

    def getResource(self) -> str:
        return self.__resources

    def getAmount(self) -> int:
        return self.__amount

    def setResource(self, res: str):
        self.__resources = res

    def setAmount(self, amt: int):
        self.__amount = amt

    def to_dto(self):
        return QuestDTO(resource=self.__resources, amount=self.__amount)

    def update_from_dto(self, quest_dto):
        self.__resources = quest_dto.resource
        self.__amount = quest_dto.amount


class QuestDTO:
    def __init__(self, title: str, resource: List[Resource]):
        self.title = title
        self.resource = resources
