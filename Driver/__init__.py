import random
from system import *

class driver(object):
    def __init__(self , road):
        self.journey = 0
        self.roadFc = road.fa
        self.maxa = random.randint(2,3)
        self.lane = "Right"
            
        road_Vmin = road.Vmin * basicLength
        road_Vmax = road.Vmax * basicLength
        tmpHoldV = random.normalvariate(road_Vmin + (road_Vmax - road_Vmin) / 3 , 8)
        if tmpHoldV < road_Vmin:
            tmpHoldV = road_Vmin
        elif tmpHoldV > road_Vmax * 3 / 5:
            tmpHoldV = road_Vmax * 3 / 5
        self.HoldV = int(round(tmpHoldV / basicLength))
        
        tmpMaxV = random.normalvariate(road_Vmin + (road_Vmax - road_Vmin) / 2 , 20)
        if tmpMaxV < tmpHoldV:
            tmpMaxV = tmpHoldV
        elif tmpMaxV > road_Vmax:
            tmpMaxV = road_Vmax
        self.MaxV = int(round(tmpMaxV / basicLength))
        
        self.velocity = self.HoldV
        self.nextVelocity = self.velocity
        
        self.crashTime = 0
        self.option = "move"
        
        self.ThisBefore = None
        self.ThisAfter = None
        
        self.OtherBefore = None
        self.OtherAfter = None