import simpy

from .Person import Person
from settings import config



def init_env(configs=config):
    """ Init the environment of simulation with configurated vars 
    """
    # SETUP SIMULATION 
    env     = simpy.Environment()
    outside = simpy.Resource(env, config['simulation']['population'])

    # CREATE OUR POPULATION
    for i in range(configs['simulation']['population']):
        Person(env, name=i, duration=configs['simulation']['duration'], outside=outside, **configs['simulation']['people'])

    return env
