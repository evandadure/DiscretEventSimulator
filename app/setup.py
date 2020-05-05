from settings import config
from .Person import Person
from .Virus import Virus



# INIT POPULATION
def create_population(env):
    """
    """
    population = []
    for i in range(config['simulation']['population']):
        p = Person(
            env, 
            name=i,
            **config['simulation']['people'], 
            infected_rate=config['simulation']['infected_rate']
        )
        population.append(p)

    return population



# INIT VIRUS
virus = Virus(**config['simulation']['virus'])