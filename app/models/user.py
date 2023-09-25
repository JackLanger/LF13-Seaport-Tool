from typing import List
from app.models.ship import Ship
from app.models.quest import Quest


class User:
    def __init__(self):
        self.__id = 0
        self.__quests: List[Quest] = []
        self.__ships: List[Ship] = []

    def getId(self) -> int:
        return self.__id

    def getQuests(self) -> List[Quest]:
        return self.__quests

    def getShips(self) -> List[Ship]:
        return self.__ships

    def setId(self, id: int):
        self.__id = id

    def setQuests(self, quests: List[Quest]):
        self.__quests = quests

    def setShips(self, ships: List[Ship]):
        self.__ships = ships

    def addQuest(self, quest: Quest):
        self.__quests.append(quest)

    def removeQuest(self, quest: Quest):
        self.__quests.remove(quest)

    def addShip(self, ship: Ship):
        self.__ships.append(ship)

    def removeShip(self, ship: Ship):
        self.__ships.remove(ship)

    def to_dto(self):
        return UserDTO(id=self.__id, quests=self.__quests, ships=self.__ships)

    def update_from_dto(self, user_dto):
        self.__id = user_dto.id
        self.__quests = user_dto.quests
        self.__ships = user_dto.ships

class UserDTO:
    def __init__(self, id: int, quests: List[Quest], ships: List[Ship]):
        self.id = id
        self.quests = quests
        self.ships = ships
