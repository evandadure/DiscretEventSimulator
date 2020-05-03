


class Virus(object):
    """
    """

    def __init__(self, name: str, infectivity: float, mortality: float, incubation: int, sick_time: int, infectivity_time: int, immunity_time: int):
        """
        """
        self.name = name
        self.infectivity = infectivity
        self.mortality = mortality
        self.incubation = incubation
        self.sick_time = sick_time
        self.infectivity_time = infectivity_time
        self.immunity_time = immunity_time


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

