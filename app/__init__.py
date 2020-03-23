import simpy

from .tuto import Car


def create_env():
    """
    """
    env = simpy.Environment()
    car = Car(env)

    return env
