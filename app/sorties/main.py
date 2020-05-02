import matplotlib.pyplot as plt
import random




def courbe_evol(liste_abs,liste_ord,nom_abs,nom_ord):
    plt.plot(liste_abs, liste_ord)
    plt.xlabel(nom_abs)
    plt.ylabel(nom_ord)
    plt.show()

def courbe_evol_cumul(liste_abs,liste_ord,nom_abs,nom_ord):
    


days = range(20)
nb_infected = [random.randrange(30, 50, 1) for i in range(20)]

courbe_evol(days,nb_infected,"jours","nombre d'infectés")