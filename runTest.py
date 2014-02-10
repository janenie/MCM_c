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
    for j in xrange(tmpTest1.testTime):
        tmpTest1.clearCrash()
        tmpTest1.handleCarOut()
        if pointer < totalCar and show_time[pointer] == j:
            tmpTest1.handleCarIn(drivers_list[pointer])
            pointer += 1
        tmpTest1.finish()
        tmpTest1.makeDecision()
        tmpTest1.handleCrash()
        
    f1.write("Rule : " + test_type[type_id] + " " 
        + str({"carIn" : tmpTest1.inCar , "carOut" : tmpTest1.receiveCar , "carCrash" : tmpTest1.crashCar})
        + "\n")

def init_drivers(testTime):
    inCarPro = 0
    for j in xrange(testTime):
        Probability = random.random()
        inCarPro += Probability
        if inCarPro >= 1:
            inCarPro -= 1
        if inCarPro <= PoissonCoef:
            drivers_list.append(driver(road_type))
            show_time.append(j)
            inCarPro = 0

for i in xrange(testTimes):
    PoissonCoef = basicFrequency + perTime * i
    tmpTest = test(road_type)
    drivers_list = []
    show_time = []
    init_drivers(tmpTest.testTime)
    f1.write("Road : " 
        + str({"maxv" : road_type.Vmax , "lenght" : road_type.numberOfPiece , "Time" : tmpTest.testTime , "Frequency" : PoissonCoef})
        + "\n")
    for j in xrange(type_len):
        runTest(tmpTest,j)
    f1.write("\n")
    print "Finish" + str(i+1)

f2.close()
f1.close()