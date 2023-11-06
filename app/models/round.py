from typing import Tuple, List, Dict, Any

from app.models.ship import Ship, ShipDTO


class RoundDTO:
    def __init__(self, round_data: List[Dict[str, Any]]):
        self.round_data = round_data

    def to_dict(self) -> dict:
        return {"round": self.round_data}

    @classmethod
    def from_dict(cls, data: dict):
        round_data = data.get("round", [])
        return cls(round_data)


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

    def to_dto(self):
        round_data = [{"ship": ShipDTO(ship).to_dict(), "status": status} for ship, status in self.__round]
        return RoundDTO(round_data)

    def update_from_dto(self, round_dto: RoundDTO):
        round_data = round_dto.round_data
        ships_and_statuses = [
            (Ship.from_dict(ship_data["ship"]), ship_data["status"]) for ship_data in round_data
        ]
        self.setRound(ships_and_statuses)
