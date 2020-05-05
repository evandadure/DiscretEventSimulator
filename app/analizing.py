import json
import numpy as np

from .Person import data



def printResults():
    """
    """
    global data
    print(json.dumps(data, indent=4))


def getNbInfectedPerPeriod(nb_period, population):
    """
    """
    global data
    #--------debug
    ppl_infected = [0] * population
    infection_list = [0] * nb_period
    tt = data
    for infection in data:
        #--------debug
        if not isinstance(ppl_infected[int(infection['id'])], list):
            ppl_infected[int(infection['id'])] = [int(infection['id'])]
        ppl_infected[int(infection['id'])].append([infection['infected_at'], infection['infected_by']])
        #--------debug

        period = infection['infected_at']
        infection_list[period]+=1
    #--------debug
    ppl_infected = list(filter((0).__ne__, ppl_infected)) #[id de la personne, [heure d'infection, source d'infection],...]
    #--------debug

    return infection_list





def getResults():
    """
    """
    global data
    return data