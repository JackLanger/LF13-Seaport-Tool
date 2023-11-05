from typing import Tuple, List

from app.models.ship import Ship


class Round:
    def __init__(self):
        self.__round: List[Tuple[Ship, str]] = []

    def setRound(self, r: List[Tuple[Ship, str]]):
        self.__round = r

    def addShip(self, r: Tuple[Ship, str]):
        self.__round.append(r)

    def removeShip(self, r: Tuple[Ship, str]):
        self.__round.remove(r)

    def clearRound(self):
        self.__round = []

    def getRound(self) -> List[Tuple[Ship, str]]:
        return self.__round