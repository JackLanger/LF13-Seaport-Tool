from quest import Quest, QuestDTO
from ship import Ship, ShipDTO
from user import User, UserDTO
from app.dal.dal import Dal


class Controler:
    def __init__(self) -> None:
        pass

    def save(data):
        Dal.serialize(data)

    def load(data):
        return Dal.deSerialize(data)

    # suply questsolver with what it needs
    def solver():
        pass

    # placeholder to speak to view
    def sendToView():
        pass

    def getFromView():
        pass
