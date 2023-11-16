from uuid import uuid4
from typing import List
import time,itertools

class Resource:
    def __init__(self, name: str, amount: int = 0):
        self.name = name
        self.amount = amount     
        
class QuestDTO:
    def __init__(self,title: str, resources: List[Resource]):
        self.id = uuid4
        self.title = title
        self.resource = resources
        
class ShipDTO:
    def __init__(self, ship_id: int, name: str, capacity: int, sailors: int, level: int = 1):
        self.id = ship_id
        self.name = name
        self.capacity = capacity
        self.sailors = sailors
        self.level = level
        self.storage = []

s= [ShipDTO(1, "Ship 0", 10, 5, 1),ShipDTO(1, "Ship 1", 10, 5, 1),ShipDTO(2, "Ship 2", 100, 15, 5),ShipDTO(3, "Ship 3", 110, 7, 3),ShipDTO(4, "Ship 4", 90, 5, 2),ShipDTO(5, "Ship 5", 20, 1, 4)]
q = QuestDTO("test",[Resource("stein",123),Resource("eisen",78),Resource("stahl",150),Resource("holz",40),Resource("kohle",250)])

class LocalResource:
    def __init__(self,name):
        self.name = name
        
class Package:
    def __init__(self,package):
        self.content = package.amount*[LocalResource(package.name)]
        self.name = package.name
        self.amount = package.amount
    
    # um pass by reference zu umgehen
    def restoreObject(self):
        self.content = self.amount*[LocalResource(self.name)]

class CapCrit:
    def __init__(self,ships,quest):
        self.perShips = ships
        self.perQuest = []
        
        for q in quest.resource:
            self.perQuest.append(Package(q))
            
    def questPermutation(self):
        return list(itertools.permutations(self.perQuest))
        
    def shipPermutation(self):
        return list(itertools.permutations(self.perShips))
    
    def getBest(self,rounds):
        rounds = list(rounds for rounds, _ in itertools.groupby(rounds))
        
        for round in rounds:
            if len(round) > len(min(rounds, key=len)):
                rounds.remove(round)      

        return rounds
        
    
    def permutate(self):
        round = []
        for quests in self.questPermutation():
            for ships in self.shipPermutation():
                round.append(self.calculate(ships,quests))
                for quest in quests:
                    quest.restoreObject()
        print(len(round))
        result = self.getBest(round)
        print(len(result))
        return result
                

    def calculate(self,ships,quest,n = 0):
        localShips = list(ships)
        localQuest = list(quest)
        shipList = []
        smallestShip = min(localShips, key=lambda x: x.capacity)
        numberOfShips = len(localShips)
        counter = 0
        
        while localQuest:
            package = localQuest[0]
            ship = localShips[n%numberOfShips]
            
            if package.content:
                if len(package.content) >= ship.capacity:
                    counter = 0
                    for _ in range(ship.capacity):
                        ship.storage.append(package.content.pop())
                    shipList.append((str(ship.name),str(package.name)))
                    ship.storage.clear()
                    n+=1
                else:
                    counter+=1
                    n+=1
                    
                if counter == numberOfShips:
                    counter = 0
                    for _ in range(len(package.content)):
                        smallestShip.storage.append(package.content.pop())
                    shipList.append((str(smallestShip.name),str(package.name)))
                    ship.storage.clear()
                    n+=1
            else:
                localQuest.pop(0)
                counter = 0
                ship.storage.clear()
                
        return shipList
    
    
res = CapCrit(s,q)
glu = res.permutate()


    