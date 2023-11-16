import uuid
from typing import List
from flask import jsonify
from .ship import ShipDTO
from .quest import QuestDTO


class UserDTO:
    def __init__(
        self, user_id: uuid, name: str, quests: List[QuestDTO], ships: List[ShipDTO]
    ):
        self.id = user_id
        self.name = name
        self.quests = quests
        self.ships = ships

    def json(self):
        ships = [ship.json() for ship in self.ships]
        quests = [quest.json() for quest in self.quests]
        return jsonify(id=self.id, name=self.name, ships=ships, quests=quests)
