import simpy
import math
import random



def getDifference(l1 = [], l2 = []):
    """ Get unique elements in l1 without the ones in common with l2.
    """
    return list(set(l1) - set(l2))



class Person(object):
    """
    """

    def __init__(self, env: simpy.Environment, name: int, duration: int, outside: simpy.Resource, trip_freq: list, trip_duration: list, nb_meeting: list) -> None:
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
        self.action = env.process(self.live(outside))
        


    def live(self, outside):
        """ Define the behavior of a person in the simulation.
        """
        while True:     
            # Wait to fit the defined frequence of trip
            yield self.env.timeout(self.trip_freq)

            # trip
            print("{} begins an outside trip at {}".format(self.id, self.env.now))
            yield self.env.process(self.go_out(self.trip_duration, outside))
            print("{} gets back at home at {}, {} people met".format(self.id, self.env.now, [p.id for p in self.met]))  ##TODO : refresh met list

            # re-initialize met people
            self.met = []



    def go_out(self, duration, outside):
        """ Go outside for a defined time.
        """
        with outside.request() as req:
            yield req
            print('NB PEOPLE OUTSIDE : {} on {}'.format(outside.count, outside.capacity))
            print('PEOPLE OUTSIDE : {}'.format(outside.users))
            # begining to meet people               
            yield self.env.process(self.meet_people(duration, outside))



    def meet_people(self, duration, outside):
        """ Meet some people that went out too.
        """
        tmp, notmet = [], []
        p = None

        for i in range(self.nb_meeting):
            tmp = outside.users
            if tmp:
                tmp.remove(self)                                     # avoid self-meeting
                notmet = getDifference(tmp, self.met)                # get people not met yet
                if notmet:
                    p = notmet[random.randint(0, len(notmet)-1)]     # choose someone randomly among not met people
                    self.met.append(p)                               # add him to met people

        print("{} meets {} people".format(self.id, len(self.met))) 
        yield self.env.timeout(duration)
            



# Launch for tutorial purposes only
if __name__ == "__main__":
    
    duration = 20
    nbpeople = 5
    env = simpy.Environment()
    outside = simpy.Resource(env, nbpeople)
    

    conf = {
        'trip_freq'     : [2, 5],
        'trip_duration' : [1, 8],
        'nb_meeting'    : [3, 5]
    }
    
    for i in range(nbpeople):
        Person(env, name=i, duration=duration, outside=outside, **conf)

    env.run(until=duration)