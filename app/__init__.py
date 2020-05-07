import simpy

from settings import config
from .processing.analizing import *
from .processing.plots import *



def create_population(env):
    """
    """
    from .simulation.Person import Person

    population = []
    for i in range(config['simulation']['population']):
        p = Person(
            env, 
            name=i,
            **config['simulation']['people'], 
            infected_rate=config['simulation']['infected_rate'],
            mask_rate = config['simulation']['mask_rate']
        )
        population.append(p)

    return population



# SIMULATION ENV
def init_env():
    """ Init the environment of simulation with configurated vars 
    """
    env = simpy.Environment()               # setup env
    population = create_population(env)     # create our population

    return env
