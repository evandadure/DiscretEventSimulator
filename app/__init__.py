import simpy

from .tuto import car


def create_env():
    """
    """
    env = simpy.Environment()
    env.process(car(env))

    return env
