from typing import List, Dict, Any

from app.models.round import Round, RoundDTO


class SolutionDTO:
    def __init__(self, solution_data: List[Dict[str, Any]]):
        self.solution_data = solution_data

    def to_dict(self) -> dict:
        return {"solution": self.solution_data}

    @classmethod
    def from_dict(cls, data: dict):
        solution_data = data.get("solution", [])
        return cls(solution_data)


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

    def to_dto(self):
        solution_data = [round_.to_dto().to_dict() for round_ in self.__solution]
        return SolutionDTO(solution_data)

    def update_from_dto(self, solution_dto: SolutionDTO):
        solution_data = solution_dto.solution_data
        rounds = [Round().update_from_dto(RoundDTO.from_dict(round_data)) for round_data in solution_data]
        self.setSolution(rounds)
