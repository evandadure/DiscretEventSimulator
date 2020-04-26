import simpy
import random



class Person(object):
    """
    """

    def __init__(self, env, name):
        """
        """
        # attributes
        self.id = name
        self.trip_duration = random.randint(1, 8)
        self.nb_meeting = random.randint(1, 5)
        self.nb_met = 0
        # simpy
        self.env = env
        self.action = env.process(self.live())
        

    def live(self):
        """
        """
        while True:
            # TRIP
            print("{} begins an outside trip at {}".format(self.id, self.env.now))
            yield self.env.process(self.go_out(self.trip_duration))
            print("{} gets back at home at {}, {} people met".format(self.id, self.env.now, self.nb_met))
            # WAITING
            yield self.env.timeout(3)


    def go_out(self, duration):
        """
        """
        yield self.env.process(self.meet_people(duration))
    

    def meet_people(self, duration):
        """
        """
        for i in range(self.nb_meeting):
            yield self.env.timeout(random.randint(1, 3))
            self.nb_met += 1
        print("{} meets people at {}".format(self.id, self.env.now))
        yield self.env.timeout(duration)
            


if __name__ == "__main__":
    
    env = simpy.Environment()
    
    for i in range(3):
        Person(env, i)

    env.run(until=20)