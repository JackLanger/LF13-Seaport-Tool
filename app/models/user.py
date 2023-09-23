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