import simpy
import random as rd

from .tuto import Car, driver
from settings import config
from .person import Person





def create_env():
    """
    """
    env = simpy.Environment()
    person = Person(
        env,
        config['environment']['people']['age_cat'],
        0,
        config['environment']['people']['health'],
        rd.randint(*config['environment']['people']['nb_meeting']),
        rd.randint(*config['environment']['people']['trip_freq']),
        0
    )


    car = Car(env)
    env.process(driver(env, car))

    return env
