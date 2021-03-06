


class Virus(object):
    """
    """

    def __init__(self, name: str, infectivity: float, mortality: float, incubation: int,
                 infect_incr: bool, sick_time: int, infectivity_time: int, immunity_time: int,
                 incubation_rate: float, sickness_rate: float):
        """
        """
        self.name = name
        self.infectivity = infectivity
        self.mortality = mortality
        self.incubation = incubation
        self.infect_incr = infect_incr
        self.sick_time = sick_time
        self.infectivity_time = infectivity_time
        self.immunity_time = immunity_time
        self.incubation_rate = incubation_rate
        self.sickness_rate = sickness_rate


    def getName(self):
        """
        """
        return self.name

    
    def getInfectivity(self):
        """
        """
        return self.infectivity


    def getMortality(self):
        """
        """
        return self.mortality

    
    def getIncubation(self):
        """
        """
        return self.incubation


    def getSickTime(self):
        """
        """
        return self.sick_time


    def getInfectivityTime(self):
        """
        """
        return self.infectivity_time

    
    def getImmunityTime(self):
        """
        """
        return self.immunity_time


    def getIncubationRate(self):
        """
        """
        return self.incubation_rate


    def getSicknessRate(self):
        """
        """
        return self.sickenss_rate



    def isInIncubation(self, person, envtime):
        """ Check if person is in incubation state
        """
        isIncubated = False
        if (envtime - person.infected_at) <= self.incubation:
            isIncubated = True
        return isIncubated


    def isSick(self, person, envtime):
        """ Check if person is in sickess state
        """
        isSick = False
        if ((envtime - person.infected_at) > self.incubation) and ((envtime - person.infected_at) <= self.sick_time):
            isSick = True
        return isSick


    def isContagious(self, person, envtime):
        """ Check if person is contagious
        """
        isInfective = False
        if ((envtime - person.infected_at) <= self.infectivity_time) and person.infected:
            isInfective = True
        return isInfective
