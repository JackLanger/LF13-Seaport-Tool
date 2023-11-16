import itertools
from algorithm.questProcessor import AlgoResult

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
        for quests in self.questPermutation()[::10]:
            for ships in self.shipPermutation()[::2]:
                round.append(self.calculate(ships,quests))
                for quest in quests:
                    quest.restoreObject()
        result = self.getBest(round)
        return AlgoResult(result[:10])
                

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


    