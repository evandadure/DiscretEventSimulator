import json
import numpy as np

from .Person import data



def printResults():
    """
    """
    global data
    print(json.dumps(data, indent=4))


def getNbInfectedPerPeriod(nb_period):
    """
    """
    global data
    infected_list = [0] * nb_period
    for infection in data:
        period = infection['infected_at']
        infected_list[period]+=1

    return infected_list





def getResults():
    """
    """
    global data
    return data