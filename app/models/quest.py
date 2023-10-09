class Quest:
    questList = []
    def __init__(self):
        self.__resource = ""
        self.__amount = 0
        self.questList.append(self)

    def getResource(self) -> str:
        return self.__resource

    def getAmount(self) -> int:
        return self.__amount

    def setResource(self, res: str):
        self.__resource = res

    def setAmount(self, amt: int):
        self.__amount = amt

    def to_dto(self):
        return QuestDTO(resource=self.__resource, amount=self.__amount)

    def update_from_dto(self, quest_dto):
        self.__resource = quest_dto.resource
        self.__amount = quest_dto.amount


class QuestDTO:
    def __init__(self, resource: str, amount: int):
        self.resource = resource
        self.amount = amount
