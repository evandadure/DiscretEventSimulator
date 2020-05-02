import matplotlib.pyplot as plt
from scipy import stats
import random
import numpy as np




def courbe_evol(liste_abs,liste_ord,nom_abs,nom_ord):
    plt.plot(liste_abs, liste_ord)
    plt.xlabel(nom_abs)
    plt.ylabel(nom_ord)
    plt.show()

def courbe_evol_cumul(liste_abs,liste_ord,nom_abs,nom_ord):

    liste_ord = [sum(liste_ord[:i+1]) for i,nb in enumerate(liste_ord)]
    plt.plot(liste_abs, liste_ord)
    plt.xlabel(nom_abs)
    plt.ylabel(nom_ord)
    plt.locator_params(axis='x', nbins=15)
    plt.show()

nb_days = 1200
days = range(nb_days)
nb_infected = [random.randrange(1, 50, 1) for i in range(nb_days)]



courbe_evol_cumul(days,nb_infected,"jours","nombre d'infectés")