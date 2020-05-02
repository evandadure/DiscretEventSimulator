import simpy
import math
import random


# People outside
outside = []


def getDifference(l1 = [], l2 = []):
    """ Get unique elements in l1 without the ones in common with l2.
    """
    return list(set(l1) - set(l2))



class Person(object):
    """
    """

    def __init__(self, env: simpy.Environment, name: int, duration: int, trip_freq: list, trip_duration: list, nb_meeting: list) -> None:
        """
        """
        # attributes
        self.id            = name
        self.met           = []
        self.trip_freq     = math.ceil( duration / random.randint(*trip_freq) )     # number of ticks to wait between each trip (rounded up) 
        self.trip_duration = random.randint(*trip_duration)                         # duration of each trip
        self.nb_meeting    = random.randint(*nb_meeting)                            # number of people met by trip
        # simpy
        self.env    = env
        self.action = env.process(self.live())
        


    def live(self):
        """ Define the behavior of a person in the simulation.
        """
        while True:     
            # Wait to fit the defined frequence of trip
            yield self.env.timeout(self.trip_freq)

            # trip
            print("{} begins an outside trip at {}".format(self.id, self.env.now))
            yield self.env.process(self.go_out(self.trip_duration))
            print("{} gets back at home at {}, {} people met".format(self.id, self.env.now, [p.id for p in self.met]))  ##TODO : refresh met list

            # re-initialize met people
            self.met = []



    def go_out(self, duration):
        """ Go outside for a defined time.
        """
        # notify the exit in the global list
        global outside
        outside.append(self)
        print('People outside : ', [p.id for p in outside])
        # begining to meet people               
        yield self.env.process(self.meet_people(duration))
        outside.remove(self)                                 # not outside anymore



    def meet_people(self, duration):
        """ Meet some people that went out too.
        """
        tmp, notmet = [], []
        p = None

        for i in range(self.nb_meeting): 
            global outside
            if outside:
                tmp = outside.copy()
                tmp.remove(self)                                     # avoid self-meeting
                notmet = getDifference(tmp, self.met)                # get people not met yet
                if notmet:
                    p = notmet[random.randint(0, len(notmet)-1)]     # choose someone randomly among not met people
                    ##TODO : do a symetric meeting
                    self.met.append(p)                               # add him to met people
                    

        print("{} meets {} people".format(self.id, len(self.met))) 
        yield self.env.timeout(duration)


    
    def infect(self, p1):
        """
        """
        return 0
            



# Launch for tutorial purposes only
if __name__ == "__main__":
    
    env = simpy.Environment()
    duration = 20

    conf = {
        'trip_freq'     : [2, 5],
        'trip_duration' : [1, 8],
        'nb_meeting'    : [3, 5]
    }
    
    for i in range(5):
        Person(env, name=i, duration=duration, **conf)

    env.run(until=duration)