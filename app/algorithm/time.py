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

ships = [ShipDTO(1, "Ship 0", 10, 5, 1),ShipDTO(1, "Ship 1", 10, 5, 1),ShipDTO(2, "Ship 2", 100, 15, 5),ShipDTO(3, "Ship 3", 110, 7, 3),ShipDTO(4, "Ship 4", 90, 5, 2),ShipDTO(5, "Ship 5", 20, 1, 4)]
quest = QuestDTO("test",[Resource("stein",120),Resource("eisen",70),Resource("stahl",150),Resource("holz",40),Resource("kohle",250)])

class LocalResource:
    def __init__(self,name):
        self.name = name
        
class Package:
    def __init__(self,package):
        self.content = package.amount*[LocalResource(package.name)]
        self.name = package.name

class TimeCrit:
    def __init__(self,ships,quest):
        self.ships = ships
        self.quest = []
        self.round = []
        
        for q in quest.resource:
            self.quest.append(Package(q))
        
        self.quest.sort(key=lambda x: len(x.content), reverse=True)
        self.ships.sort(key=lambda x: x.capacity, reverse=True)
        
    def checkAllResources(self):
        amount = 0
        for package in self.quest:
            amount += len(package.content)
        return amount
    
    def checkResource(self,ship,resource):
        if not ship.storage or ship.storage[0].name == resource.name:
            return True
        else:
            return False
        
    def forJack(self,input):
        output = [[] for x in range(len(input)//len(self.ships)+1)]
        for i in range(len(input)):
            output[i//len(self.ships)].append(input[i])
        return output
    
    def calculate(self,n = 0):
        if n < len(self.ships):
            while self.checkAllResources() > 0:
                self.quest.sort(key=lambda x: len(x.content), reverse=True)
                package = self.quest[0]
                ship = self.ships[n]
                while len(ship.storage) < ship.capacity and len(package.content) > 0 and self.checkResource(ship,package):
                    ship.storage.append(package.content.pop())
                    
                    if len(ship.storage) == ship.capacity:
                        self.round.append((ship.name,package.name))
                        self.calculate(n+1)
                         
                    if not package.content and self.quest:
                        self.quest.pop(0)
                        self.round.append((ship.name,package.name))
                        self.calculate(n+1)
                        
                n = 0
                for ship in self.ships:
                    ship.storage.clear()
                    
        return self.forJack(self.round)
        
res = TimeCrit(ships,quest)
x = res.calculate()
print(x)



    