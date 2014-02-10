from Test import test
from copy import deepcopy as cpy
from Road import Road
from Driver import driver
from system import *
import random

f1 = open("Data/data", "w")
f2 = open("Data/density", "w")
road_type = Road()
drivers_list = []
show_time = []

def runTest(template_test,type_id):
    tmpTest1 = cpy(template_test)
    tmpTest1.setFSA(test_type[type_id])
    pointer = 0
    totalCar = len(drivers_list)
    f2.write("Rule : " + test_type[type_id] + "\n")
    for j in xrange(tmpTest1.testTime):
        tmpTest1.clearCrash()
        tmpTest1.handleCarOut()
        if pointer < totalCar and show_time[pointer] <= j:
            if tmpTest1.handleCarIn(drivers_list[pointer]):
                pointer += 1
        tmpTest1.finish()
        tmpTest1.makeDecision()
        tmpTest1.handleCrash()
        if j % 60 == 59:
            f2.write(str(len(tmpTest1.drivers) * 1.0 / tmpTest1.road.numberOfPiece))
            f2.write(" , ")
    f2.write("\n")
        
    f1.write("Rule : " + test_type[type_id] + " " 
        + str({"carIn" : tmpTest1.inCar , "carOut" : tmpTest1.receiveCar , "carCrash" : tmpTest1.crashCar})
        + "\n")

def addDriver(t):
    drivers_list.append(driver(road_type))
    show_time.append(t)

def init_drivers(testTime):
    for j in xrange(testTime):
        Probability = random.uniform(0,2.0)
        if Probability >= 1:
            addDriver(j)
            Probability -= 1
            if Probability >= basicFrequency:
                addDriver(j)
        elif Probability >= basicFrequency:
            addDriver(j)

for i in xrange(testTimes):
    #PoissonCoef = basicFrequency + perTime * i
    tmpTest = test(road_type)
    drivers_list = []
    show_time = []
    init_drivers(tmpTest.testTime)
    f1.write("Road : " 
        + str({"maxv" : road_type.Vmax , "lenght" : road_type.numberOfPiece , "Time" : tmpTest.testTime , "Frequency" : basicFrequency})
        + "\n")
    f2.write("Road : " 
        + str({"lenght" : road_type.numberOfPiece * basicLength, "Time" : tmpTest.testTime , "Frequency" : basicFrequency})
        + "\n")
    for j in xrange(type_len):
        runTest(tmpTest,j)
    f1.write("\n")
    print "Finish" + str(i+1)

f2.close()
f1.close()
