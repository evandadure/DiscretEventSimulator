import app

from settings import config



if __name__ == "__main__":

    duration = config['simulation']['duration']

    env = app.init_env()
    env.run(until=duration)

    app.printResults()

    listNbInfected = app.getNbInfectedPerPeriod(duration)
    app.courbe_evol(range(duration),listNbInfected,"Heures","Nombre d'infectés")
    app.courbe_evol_cumul(range(duration),listNbInfected,"Heures","Nombre d'infectés")
