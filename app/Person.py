import simpy
import random


# People outside
outsiders = []


def getDifference(l1 = [], l2 = []):
    """ Get unique elements in l1, but not in l2.
    """
    return list(set(l1).difference(l2))




class Person(object):
    """
    """

    def __init__(self, env, name):
        """
        """
        # attributes
        self.id  = name
        self.met = []
        self.trip_duration = random.randint(1, 8)
        self.nb_meeting = random.randint(1, 5)
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
            print("{} gets back at home at {}, {} people met".format(self.id, self.env.now, self.met))
            # WAITING
            yield self.env.timeout(3)


    def go_out(self, duration):
        """
        """
        # notify the exit in the global list
        global outsiders
        outsiders.append(self)       
        # begining to meet people                     
        yield self.env.process(self.meet_people(duration))
    

    def meet_people(self, duration):
        """
        """
        global outsiders
        tmp, notmet = [], []
        p = None

        for i in range(self.nb_meeting):
            if outsiders:
                tmp    = outsiders
                tmp.remove(self)                                        # avoid self-meeting
                notmet = getDifference(tmp, self.met)                   # get people not met yet
                if notmet:
                    p = notmet[random.randint(0, len(notmet)-1)]      # choose someone randomly among not met people
                    self.met.append(p.id)                                # add him to met people
                    print("{} meets {} at {}".format(self.id, p.id, self.env.now))
                
            # wait a bit before meeting someone else     
            yield self.env.timeout(random.randint(1, 3))

        yield self.env.timeout(duration)
            


if __name__ == "__main__":
    
    env = simpy.Environment()
    
    for i in range(20):
        Person(env, i)

    env.run(until=20)