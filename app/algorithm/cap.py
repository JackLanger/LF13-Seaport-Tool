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

class CapCrit:
    def __init__(self,ships,quest):
        self.ships = []
        self.quest = []
        
        self.perShips = ships
        self.perQuest = []
        
        self.round = []
        self.biground = []
        
        for q in quest.resource:
            self.perQuest.append(Package(q))
            
    def questPermutation(self):
        return list(itertools.permutations(self.perQuest))
        
    def shipPermutation(self):
        return list(itertools.permutations(self.perShips))
        
    def checkAllResources(self):
        amount = 0
        for package in self.perQuest:
            amount += len(package.content)
        return amount
    
    def checkResource(self,ship,resource):
        if not ship.storage or ship.storage[0].name == resource.name:
            return True
        else:
            return False
        
    def forJack(self,input):
        output = [[] for x in range(len(input)//len(self.perShips)+1)]
        for i in range(len(input)):
            output[i//len(self.ships)].append(input[i])
        return output
        
    # def permutate(self):
    #     x = self.questPermutation()
    #     y = self.shipPermutation()
    #     print(len(x[0]))
    #     print(len(y[0]))
    
    def permutate(self):
        n=0
        m=0
        for quests in self.questPermutation():
            for ships in self.shipPermutation():
                self.biground.append(self.calculate(ships,quests))
        return self.biground
                

    def calculate(self,ships,quest,n = 0,m = 0):
        localShips = list(ships)
        localQuest = list(quest)
        for i in localQuest:
            print(i.name)
        if n < len(localShips):
            while self.checkAllResources() > 0:
                ship = localShips[n]
                package = localQuest[m]
                print(ship.name,package.name,len(package.content))
                time.sleep(1)
                while len(ship.storage) < ship.capacity and len(package.content) > 0 and self.checkResource(ship,package):
                    ship.storage.append(package.content.pop())
                    
                    if len(ship.storage) == ship.capacity:
                        self.round.append((ship.name,package.name))
                        self.calculate(localShips,localQuest,n+1)
                         
                    if not package.content and localQuest:
                        # localQuest.pop(0)
                        self.round.append((ship.name,package.name))
                        self.calculate(localShips,localQuest,n+1,m+1)
                        
                n = 0
                m = 0
                for ship in self.ships:
                    ship.storage.clear()
                    
        x = self.forJack(self.round)
        print(x)
        time.sleep(1)
        return x
    
    
res = CapCrit(ships,quest)
glu = res.permutate()
# print(glu)

    