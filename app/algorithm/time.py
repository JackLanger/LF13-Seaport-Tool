import itertools
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
        
    def checkAllResources(self,quest):
        amount = 0
        for package in quest:
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
            output[i//len(self.perShips)].append(input[i])
        return output
    
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
        return self.getBest(round)
                
    def calculate(self,ships,quest,n = 0):
        localShips = list(ships)
        localQuest = list(quest)

        if n < len(localShips):
            while self.checkAllResources(localQuest) > 0:
                package = localQuest[0]
                ship = localShips[n]
                while len(ship.storage) < ship.capacity and len(package.content) > 0 and self.checkResource(ship,package):
                    ship.storage.append(package.content.pop())
                    
                    if not package.content and localQuest:
                        localQuest.pop(0)
                        self.round.append((ship.name,len(ship.storage),package.name))
                        self.calculate(localShips,localQuest,n+1)                    
                    
                    if len(ship.storage) == ship.capacity:
                        self.round.append((ship.name,len(ship.storage),package.name))
                        self.calculate(localShips,localQuest,n+1)
                                        
                n = 0
                for ship in localShips:
                    ship.storage.clear()
        return self.forJack(self.round)


    