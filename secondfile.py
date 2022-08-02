
class Gender2Statistics:

import numpy

# Snowbasin, UT
def fwinterAlpine(self,name):
    "0": {
        "codex": 6414,
        "year": 2002,
        country: "USA",
        "athleteProfile": [
            {
                "FIS": 536138,
                "name": "Clark Kirsten L"
                "totalTime": 76.67,
                fisPoints: 21.55
            }
        ]
    }
    "1": {
        "codex": 6414,
        "year": 2002,
        country: "USA",
        "athleteProfile": [
            {
                "FIS": 536477,
                "name": "Mendes Jonna"
                "totalTime": 76.91,
                fisPoints: 23.23
            }
        ]
    }
    "2": {
        "codex": 6414,
        "year": 2002,
        country: "USA",
        "athleteProfile": [
            {
                "FIS": 535529,
                "name": "Monahan Kathleen"
                "totalTime": 77.59
                fisPoints: 27.99
            }
        ]
    }
    # Finding mean on time
    fWA1 = "0"["athleteProfile"]["totalTime"]
    fWA2 = "1"["athleteProfile"]["totalTime"]
    fWA3 = "2"["athleteProfile"]["totalTime"]
    averagefWA = fWA1 + fWA2 + fWA3
    averagefwaUSA = numpy.mean(averagefWA)
    print("The average athlete's time for winter alpine is: " + str(averagefwaUSA) + ".")

# Pyenoungchang
def fskiJumping(self,name):
    "0": {
        "codex": 3097,
        "year": 2018,
        country: "South Korea",
        "athleteProfile": [
            {
                "FIS": 5399,
                "name": "Hendrickson Sarah",
                "totalDistance": 87
                fisPoints: 160.6
            }
        ]
    }
    "1": {
        "codex": 3097,
        "year": 2018,
        country: "South Korea",
        "athleteProfile": [
            {
                "FIS": 2682,
                "name": "Ringquist Abby",
                "totalDistance": 84.25
                fisPoints: 144.4
            }
        ]
    }
"2": {
    "codex": 3097,
    "year": 2018,
    country: "South Korea",
    "athleteProfile": [
        {
            "FIS": 6089,
            "name": "Engulnd Nita"
            "totalDistance": 77
            fisPoints: 57.9
        }
    ]
}

# Finding mean of ski jumping distance
fSJ1 = "0"["athleteProfile"]["totalDistance"]
fSJ2 = "1"["athleteProfile"]["totalDistance"]
fSJ3 = "2"["athleteProfile"]["totalDistance"]
averageFSJ = fSJ1 + fSJ2 + fSJ3
fsjUSA = numpy.mean(averageFSJ)
print("The average athelte's ski jumping distance is: " + str(averageFSJ) + ".")

    def fwinterRunning(self):
        "0": {
            "codex": 2856,
            "year": 1970,
            country: "USA",
            "athleteProfile": [
                {
                    "FIS": 1004338,
                    "name": "Kemppell Nina",
                    "totalTime": 114.14,
                    fisPoints: 53.81
                }
            ]
        }
        "1": {
            "codex": 2856,
            "year": 1973,
            country: "USA",
            "athleteProfile": [
                {
                    "FIS": 1155658,
                    "name": "Wagner Wendy Kay",
                    "totalTime": 108.125
                }
            ]
        }
        "2": {
            "codex": 2856,
            "year": 1977,
            country: "USA",
            "athleteProfile": [
                {
                    "FIS": 1196107,
                    "name": "Jones Barbara",
                    "totalTime": 119.403
                }
            ]
        }

# Finding mean on f-running time

fwr1 = "0"["athleteProfile"]["totalTime"]
fwr2 = "1"["athleteProfile"]["totalTime"]
fwr3 = "2"["athleteProfile"]["totalTime"]
averagefwr = fwr1 + fwr2 + fwr3
fwrUSA = numpy.mean(averagefwr)
print("The average athlete's distance for running is: " + str(fwrUSA) + ".")
