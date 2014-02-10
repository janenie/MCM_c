import random
from system import *

class FSA(object):
    def __init__(self):
        return
        
    def decideLane(self,driver):
        driver.lane = "Right"
    
    def judge(self,driver):
        velocity = driver.velocity
        accelorate = max(1 , driver.maxa - driver.roadFc)
        moderate = max(1 , driver.roadFc)
        
        if driver.option == "crash":
            driver.nextVelocity = max(0,velocity - moderate)
            return "crash"

        if driver.ThisBefore == None:
            ThisBeforeDis = bigV
        else:
            ThisBeforeDis = driver.ThisBefore.journey - driver.journey
        
        if driver.OtherBefore == None:
            OtherBeforeDis = bigV
        else:
            OtherBeforeDis = driver.OtherBefore.journey - driver.journey
        
        if driver.ThisAfter == None:
            ThisAfterDis = bigV
        else:
            ThisAfterDis = driver.journey - driver.ThisAfter.journey
            
        if driver.OtherAfter == None:
            OtherAfterDis = bigV
        else:
            OtherAfterDis = driver.journey - driver.OtherAfter.journey
        
        if ThisBeforeDis < 0: 
            print "ThisBefore"
        if ThisAfterDis < 0:
            print "ThisAfter"
        if OtherBeforeDis < 0:
            print "OtherBefore"
        if OtherAfterDis < 0:
            print "OtherAfter"
        
        driver.nextVelocity = min(velocity + accelorate , driver.MaxV , ThisBeforeDis - 1)
        #driver.nextVelocity = max(driver.nextVelocity , velocity - moderate)
        
        lane = driver.lane
        
        if driver.OtherAfter == None:
            OtherAfterV = 0
        else:
            OtherAfterV = driver.OtherAfter.velocity

        if OtherAfterV < OtherAfterDis - 1:
            if velocity > ThisBeforeDis - 1 and OtherBeforeDis > ThisBeforeDis:
                driver.nextVelocity = min(velocity + accelorate , driver.MaxV , OtherBeforeDis - 1)
                return "changeLane"
                
        return "move"
