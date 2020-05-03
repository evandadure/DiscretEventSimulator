import simpy
import math
import random

data = []           # Monitored data
people  = []        # List of every people
outside = []        # List of outside people


def getDifference(l1 = [], l2 = []):
    """ Get unique elements in l1 without the ones in common with l2.
    """
    return list(set(l1) - set(l2))



class Person(object):
    """
    """

    def __init__(self, env: simpy.Environment, name: int, duration: int, trip_freq: list, trip_duration: list, nb_meeting: list, infected_rate: float) -> None:
        """
        """
        # ATTRIBUTES
        self.id            = name
        self.met           = set([])
        self.infections    = []                                                     # data about sucessful infections
        self.trip_freq     = math.ceil( duration / random.randint(*trip_freq) )     # number of ticks to wait between each trip (rounded up) 
        self.trip_duration = random.randint(*trip_duration)                         # duration of each trip
        self.nb_meeting    = random.randint(*nb_meeting)                            # number of people met by trip
        self.infected      = True if random.random() <= infected_rate else False    # Chance of being infected from start
        self.infector      = None
        self.infected_at   = 0
        self.mask_on       = True if random.random() <= 0.5 else False
        self.dead          = False

        # BASE MONITORING
        if self.infected:
            global data
            data.append({'id': str(self.id), 'infected_at': self.infected_at, 'infected_by': 'primary infection'})

        # SIMPY
        global people
        people.append(self)
        self.env    = env
        self.action = env.process(self.live())



    def printStats(self):
        """
        """
        inf = "infected by {} at {}".format(self.getInfector(), self.infected_at) if self.infected else "clean"
        print(f"================ STATS of : {self.id} ================")
        print("{} people met : {}".format(len(self.met), [p.id for p in self.met]))
        print("State : {}".format(inf))
        print("People infected : ", [p['id'] for p in self.infections])
        print("=======================================================")
        


    def live(self):
        """ Define the behavior of a person in the simulation.
        """
        while True:     
            # Wait to fit the defined frequence of trip
            yield self.env.timeout(self.trip_freq)

            # trip
            print("{} begins an outside trip at {}".format(self.id, self.env.now))
            yield self.env.process(self.go_out(self.trip_duration))
            print("{} gets back at home at {}".format(self.id, self.env.now))
            self.printStats()

            # re-initialize met people
            self.met = set([])



    def go_out(self, duration):
        """ Go outside for a defined time.
        """
        # notify the exit in the global list
        global outside
        outside.append(self)
        print('People outside : ', [p.id for p in outside])

        # starting to meet people            
        for i in range(self.nb_meeting):
            self.meet_people()
        
        yield self.env.timeout(duration)
        outside.remove(self)               # not outside anymore



    def meet_people(self):
        """ Meet some people that went out too.
        """
        tmp, notmet = [], []
        p = None

        global outside
        if outside:
            tmp = outside.copy()
            tmp.remove(self)                                     # avoid self-meeting
            notmet = getDifference(tmp, self.met)                # get people not met yet
            if notmet:
                p = notmet[random.randint(0, len(notmet)-1)]     # choose someone randomly among not met people
                self.met.add(p)                                  # add him to met people
                global people
                people[people.index(p)].met.add(self)            # symetric meeting
                # INFECTION TEST
                self.infection(p)



    def infection(self, p):
        """
        """
        # At least one is not infected
        if not (self.infected and p.infected):
            infector = self if self.infected else p if p.infected else None     # infector is self or p, else None
            if infector:
                if self.getInfectionRate() > random.random():
                    infected = self if infector == p else p             # infected is self or p
                    infected.setInfectionAttr(infector, self.env.now)   # set infection
                    # RECORD / MONITORING
                    record = {'id': str(infected.id), 'infected_at': self.env.now, 'infected_by': str(infector.id)}
                    self.monitoring(record)
                    infector.infections.append(record)                  # local save
                    print("{} infects {} at {}".format(infector.id, infected.id, self.env.now))
                else:
                    almost_infected = self if infector == p else p
                    print(f"{infector.id} failed to infect {almost_infected.id} with infectivity rate : {infector.getInfectionRate()}")
        else:
            ## monitor 0 infection case ?
            pass



    def setInfectionAttr(self, infector, time):
        """
        """
        self.infected = True
        self.infector = infector
        self.infected_at = time


    
    def getInfectionRate(self):
        infectRate = 1          # Virus infectivity
        if self.mask_on:
            infectRate -= 0.5   # Mask efficiency
        return infectRate
        


    def getInfector(self):
        """ Return the person who transmitted the infection
        """
        return self.infector.id if isinstance(self.infector, Person) else None


    def monitoring(self, record: dict):
        """
        """
        global data
        data.append(record)




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
        print(type(Person(env, name=i, duration=duration, **conf)))
        

    # env.run(until=duration)