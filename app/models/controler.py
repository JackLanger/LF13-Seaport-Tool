from quest import Quest, QuestDTO
from ship import Ship,ShipDTO
from user import User, UserDTO
from app.dal.dal import Dal


class Controler:
    def __init__(self) -> None:
        self.__userlist = []
        self.__shiplist = []
        self.__questlist = []
        
    def getUserList(self):
        return self.__userlist
    
    def getShipList(self):
        return self.__shiplist
    
    def getQuestList(self):
        return self.__questlist
    
    def addUser(self,user):
        self.__userlist.append(user)
        
    def addShip(self,ship):
        self.__shiplist.append(ship)
        
    def addQuest(self,quest):
        self.__questlist.append(quest)
        
    def removeUser(self,user):
        self.__userlist.remove(user)
        
    def removeShip(self,ship):
        self.__shiplist.remove(ship)
        
    def removeQuest(self,quest):
        self.__questlist.remove(quest)
        
    def saveList(list):
        Dal.serialize(list)
    
    def loadList():
        return Dal.deSerialize()
    
    def solver():
        pass
    
    def sendToView():
        pass
    
    def getFromView():
        pass
    
    def createUser():
        pass
    
    def createQuest():
        pass
    
    def createShip():
        pass