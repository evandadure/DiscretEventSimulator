import simpy

from .Person import Person



def init_env(configs: dict):
    """ Init the environment of simulation with configurated vars 
    """
    env = simpy.Environment()

    # CREATE OUR POPULATION
    for i in range(configs['simulation']['population']):
        Person(env, name=i, duration=configs['simulation']['duration'], **configs['simulation']['people'], hc_rate=configs['simulation']['hc_rate'])

    return env
