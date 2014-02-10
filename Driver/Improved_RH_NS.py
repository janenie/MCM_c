import random
from system import *

class driveFSA(object):
    def __init__(self, driver):
        self.driver = driver
        self.nowStatus = {
                             "lane": "Right",
                         }
    
    def judge(self):
        velocity = self.driver.velocity
        accelorate = max(1 , self.driver.maxa - self.driver.roadFc)
        moderate = max(1 , self.driver.maxa + self.driver.roadFc)
        
        if self.driver.option == "crash":
            self.driver.nextVelocity = velocity - moderate
            return "crash"

        if self.driver.ThisBefore == None:
            ThisBeforeDis = bigV
        else:
            ThisBeforeDis = self.driver.ThisBefore.journey - self.driver.journey + self.driver.ThisBefore.velocity
        
        if self.driver.OtherBefore == None:
            OtherBeforeDis = bigV
        else:
            OtherBeforeDis = self.driver.OtherBefore.journey - self.driver.journey
        
        if self.driver.ThisAfter == None:
            ThisAfterDis = bigV
        else:
            ThisAfterDis = self.driver.journey - self.driver.ThisAfter.journey
            
        if self.driver.OtherAfter == None:
            OtherAfterDis = bigV
        else:
            OtherAfterDis = self.driver.journey - self.driver.OtherAfter.journey
        
        self.driver.nextVelocity = min(velocity + accelorate , self.driver.MaxV , ThisBeforeDis - 1)
        self.driver.nextVelocity = max(self.driver.nextVelocity , velocity - moderate)
        
        lane = self.nowStatus["lane"]
        
        if self.driver.OtherAfter == None:
            OtherAfterV = 0
        else:
            OtherAfterV = self.driver.OtherAfter.velocity
        
        if OtherAfterV < OtherAfterDis - 1:
            if lane == "Right":
                if velocity > ThisBeforeDis - 1 and OtherBeforeDis > ThisBeforeDis:
                    return "changeLane"
            else:
                if velocity < OtherBeforeDis - 1:
                    return "changeLane"

        return "move"