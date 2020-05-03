import simpy
from .Person import Person
from settings import config


def init_env():
    """ Init the environment of simulation with configurated vars 
    """
    env = simpy.Environment()


    # CREATE OUR POPULATION
    for i in range(config['simulation']['population']):
        Person(env, 
            name=i, 
            duration=config['simulation']['duration'], 
            **config['simulation']['people'], 
            infected_rate=config['simulation']['infected_rate'])


    return env
