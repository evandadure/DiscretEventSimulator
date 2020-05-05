import simpy

from .setup import create_population
from .analizing import *
from .plots import *



def init_env():
    """ Init the environment of simulation with configurated vars 
    """
    env = simpy.Environment()               # setup env
    population = create_population(env)     # create our population

    return env
