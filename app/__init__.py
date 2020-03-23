import simpy

from .tuto import Car, driver


def create_env():
    """
    """
    env = simpy.Environment()
    car = Car(env)
    env.process(driver(env, car))

    return env
