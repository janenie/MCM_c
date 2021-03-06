import random
from system import *

VLimit = [(40 / 3.6, 80 / 3.6), (40 / 3.6, 120 / 3.6),
          (60 / 3.6, 120 / 3.6), (60 / 3.6, 160 / 3.6),
          (80 / 3.6, 160 / 3.6)]
ROADTYPE = ["asphalt", "concrete", "gravel"]
FC = {
         ("asphalt", "dry"): 0.675, 
         ("asphalt", "wet"): 0.45, 
         ("concrete", "dry"): 0.62,
         ("concrete", "wet"): 0.485,
         ("gravel", "dry"): 0.5,
         ("gravel", "wet"): 0.35,
     }
g = 9.83218
     
#0 for straight , 1 for Curve
class Road(object):
    def __init__(self):
        self.numberOfPiece = random.randint(minNumOfPiece,maxNumOfPiece)
        self.piece = []
        self.g = g
        flag = 0
        for i in xrange(self.numberOfPiece):
          if flag > 0:
            self.piece.append(1)
            flag -= 1
            continue
          Probability = random.random()
          if Probability < ProbabilityOfCurve:
            flag = random.randint(1,maxCurveNum)
            self.piece.append(0)
          else:
            self.piece.append(1)
        
        for i in xrange(5):
            if Probability <= (i + 1) * 0.2:
                (road_Vmin, road_Vmax) = VLimit[i]
                break
        self.Vmin = int(round(road_Vmin / basicLength))
        self.Vmax = int(round(road_Vmax / basicLength))
        self.Vmin = 1
        self.Vmax = roadMaxV
        Probability = random.random()
        if Probability <= 0.5:
            road_type = ROADTYPE[0]
        elif Probability <= 0.9:
            road_type = ROADTYPE[1]
        else:
            road_type = ROADTYPE[2]
        Probability = random.random()
        if Probability <= 0.5:
            road_weather = "dry"
        else:
            road_weather = "wet"
        self.weather = road_weather
        road_fc = FC[(road_type, road_weather)]
        self.fa = int(round(g * road_fc / basicLength / timesPerSecond))