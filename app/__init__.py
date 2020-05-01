import simpy

from .Person import Person
from settings import config


env     = simpy.Environment()
outside = simpy.Resource(env, config['simulation']['population'])



def init_env(configs=config):
    """ Init the environment of simulation with configurated vars 
    """
    # CREATE OUR POPULATION
    for i in range(configs['simulation']['population']):
        Person(env, name=i, duration=configs['simulation']['duration'], **configs['simulation']['people'])

    return env
