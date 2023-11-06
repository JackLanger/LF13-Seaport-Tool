from typing import List

from app.models.quest import QuestDTO
from app.models.ship import ShipDTO
from algorithm.questProcessor import Algorithm


class TimeAlgorithm(Algorithm):
    def __init__(self, ships: List[ShipDTO], quest: QuestDTO):
        super().__init__(ships, quest)

    def calculate(self):
        print("time")
