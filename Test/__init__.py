from copy import deepcopy as cpy
from Driver import No_Rule_NS
from Driver import RightHand_NS
from system import *
import random

class test(object):
    def __init__(self,road):
        self.road = road
        self.drivers = []
        #self.testTime = int(round(road.numberOfPiece * 1.5))
        self.testTime = testTime
        self.inCar = 0
        self.receiveCar = 0
        self.crashCar = 0
        self.FSA = None
        
    def setFSA(self,FSA):
        if FSA == "RightHand_NS":
            self.FSA = RightHand_NS.FSA()
        elif FSA == "No_Rule_NS":
            self.FSA = No_Rule_NS.FSA()
    
    def handleCarIn(self,tmpCar):
        self.FSA.decideLane(tmpCar)
        self.drivers.append(cpy(tmpCar))
        self.inCar += 1

    def handleCarOut(self):
        removeList = []
        for item in self.drivers:
            if item.journey >= self.road.numberOfPiece:
                removeList.append(item)
        for item in removeList:
            self.drivers.remove(item)
            self.receiveCar += 1

    def clearCrash(self):
        removeList = []
        for item in self.drivers:
            if item.option == "crash":
                if item.crashTime <= 0:
                    removeList.append(item)
                else:
                    item.crashTime -= 1

        for item in removeList:
            self.drivers.remove(item)
            self.crashCar += 1
                
    def newMove(self,item):
        item.velocity = item.nextVelocity
        item.journey += item.velocity

    def newSwitch(self,item):
#        return 
        if item.lane == "Right":
            item.lane = "Left"
        else:
            item.lane = "Right"
        item.option = "move"
        #print "changeLane"

    def handleCrash(self):
        nextCar = {"Left" : None , "Right" : None}
        for item in self.drivers:
            lane = item.lane
            if nextCar[lane] != None:
                if item.journey <= nextCar[lane].journey:
                    if item.option != "crash":
                        item.crashTime = basicCrashTime * random.random()
                    if nextCar[lane].option != "crash":
                        nextCar[lane].crashTime = basicCrashTime * random.random()
                    item.option = nextCar[lane].option = "crash"
                    print lane
            nextCar[lane] = item
    
    def findNextCar(self,item,_id):
        length = len(self.drivers)
        nextCar = {"Left" : None , "Right" : None}
        for i in xrange(_id-1,-1,-1):
            after = self.drivers[i]
            if item.journey - after.journey > self.road.Vmax:
                break
            lane = after.lane
            if nextCar[lane] == None:
                nextCar[lane] = after
            elif after.journey > nextCar[lane].journey:
                nextCar[lane] = after
        
        lane = item.lane
        other = ""
        if lane == "Right":
            other = "Left"
        else:
            other = "Right"
        item.ThisAfter = nextCar[lane]
        item.OtherAfter = nextCar[other]
            
    def findPreCar(self,item,_id):
        length = len(self.drivers)
        preCar = {"Left" : None , "Right" : None}
        for i in xrange(_id+1,length,1):
            before = self.drivers[i]
            if before.journey - item.journey > 2 * self.road.Vmax:
                break
            lane = before.lane
            if preCar[lane] == None:
                preCar[lane] = before
            elif before.journey < preCar[lane].journey:
                preCar[lane] = before
        
        lane = item.lane
        other = ""
        if lane == "Right":
            other = "Left"
        else:
            other = "Right"
        item.ThisBefore = preCar[lane]
        item.OtherBefore = preCar[other]
        
    def makeDecision(self):
        length = len(self.drivers)
        preCar = {"Left" : None , "Right" : None}
        for i in xrange(length-1,-1,-1):
            item = self.drivers[i]
            
            self.findPreCar(item,i)
            self.findNextCar(item,i)
            
            item.option = self.FSA.judge(item)
            if item.option == "changeLane":
                self.newSwitch(item)
            self.newMove(item)

    def finish(self):
        self.drivers.sort(cmp=lambda x,y:cmp(x.journey, y.journey))
        #less first