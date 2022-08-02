#   Marvish Chandra

import numpy

class Gender1Statistics:

def __init__(self,country,totalTime,fisPoints):
    self.country = country
    self.totalTime = totalTime
    self.fisPoints = fisPoints



# top 3 US candidates
# Results from Proctor Ski Area (1st Game in WO)

def winterAlpine(self,name):
    "0":{
        "codex": 106542394,
        "year": 1999,
        country: "USA",
        "athleteProfile": [
            {
                "FIS": 1983,
                "name": "Brayton Hunter",
                "totalTime": 90.63,
                fisPoints: 41.77
            }
        ]
    }
    "1":{
        "codex": 306533028,
        "year": 2002,
        country: "USA",
        "athleteProfile": [
            {
                "FIS": 2002,
                "name": "Kearing Luke",
                "totalTime": 90.96,
                fisPoints: 44.80

            }
        ]
    }
    "2":{
        "codex": 176532584,
        "year": 2000,
        country: "USA",
        "athleteProfile": [
            {
                "FIS": 176532584,
                "name": "Underhill Bradshaw",
                "totalTime": 91.02,
                fisPoints: 45.28
            }
        ]
    }

wA1 = "0"["totalTime"]
wA2 = "1"["totalTime"]
wA3 = "2"["totalTime"]
averageWA = wA1 + wA2 + wA3
avUSA = numpy.mean(averageWA)
print("The average three scores from USA's alpine athletes is: " + str(avUSA) + ".")

# Park City, UT

def winter_Ski_Jumping(self,name):
    "0":{
      "codex": 75835,
        "year": 1984,
        "country": "USA",
        "athleteProfile": [
            "FIS": 4592,
            "name": "Welch Brian",
            "totalDistance": 313.2
            fisPoints: 755.1
        ]
    }
    "1":{
        "codex": 75835,
        "year": 1983,
        country: "USA",
        "athleteProfile": [
            "FIS": 3013,
            "name": "Schwall Tommy",
            "totalDistance": 369.6,
            fisPoints: 755.1
        ]
    }
    "2":{
        "codex": 75835,
        "year": 1984,
        country: "USA",
        "athleteProfile": [
            "FIS": 3157,
            "name": "Jones Clint",
            "totalDistance": 110.925,
            fisPoints: 755.1
        ]
    }
    "3":{
        "codex": 75835,
        "year": 1980,
        country: "USA",
        "athleteProfile": [
            "FIS": 2077,
            "name": "Alborn Alan Jacob",
            "totalDistance": 117.475
            fisPoints: 755.1
        ]

# finding mean on distance
wSJ1 = "0"["totalDistance"]
wSJ2 = "1"["totalDistance"]
wSJ3 = "2"["totalDistance"]
wSJ4 = "3"["totalDistance"]
averageSJ = wSJ1 + wSJ2 + wSJ3 + wSJ4
sJUSA = numpy.mean(averageSJ)
print("The average mean on distance for ski jumping's athlete's is: " + str(sJUSA) + ".")


# Salt Lake City
def winterRunning(self,name):
    "0":{
        "codex": 2855,
        country: "USA",
        "athleteProfile": [
            {
                "FIS": 1016754,
                "name": "Bauer John",
                "totalTime": 152.506,
                fisPoints: 64.06
            }
        ]
    }
    "1":{
        "codex": 2855,
        country: "USA",
        "athleteProfile": [
            {
                "FIS": 1285444,
                "name": "Johnson Andrew"
                "totalTime": 152.443
                fisPoints: 125.32
            }
        ]
    }
    }

    wr1 = "0"["athleteProfile"]["TotalTime"]
    wr2 = "1"["athleteProfile"]["TotalTime"]
    avWR = wr1 + wr2
    wrUSA = numpy.mean(avWR)
    print("The average running's athlete time is: " + str(wrUSA) + ".")