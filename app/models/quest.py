from typing import List


class Resource:
    def __init__(self, name: str, amount: int = 0):
        self.name = name
        self.amount: int = amount


class Quest:
    questList = []
    def __init__(self, title: str = ""):
        self.__title = title
        self.__resources = []
        self.__amount = 0
        self.questList.append(self)

    def getResource(self) -> List[str]:
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
    def __init__(self,id:int, title: str, resources: List[str]):
        self.id = id
        self.title = title
        self.resource = resources
        self.amount = resources[0].amount
