from typing import List

from app.models.round import Round


class Solution:

    def __init__(self):
        self.__solution: List[Round] = []

    def setSolution(self, s: List[Round]):
        self.__solution = s

    def addRound(self, r: Round):
        self.__solution.append(r)

    def deleteRound(self, r: Round):
        self.__solution.remove(r)

    def clearSolution(self):
        self.__solution = []

    def getSolution(self) -> List[Round]:
        return self.__solution
