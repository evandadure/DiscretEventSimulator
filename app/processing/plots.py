import matplotlib.pyplot as plt
import numpy as np




def courbe_evol(liste_abs,liste_ord,nom_abs,nom_ord):
    """
    Creating a 2D plot
    """
    plt.plot(liste_abs, liste_ord)
    plt.xlabel(nom_abs)
    plt.ylabel(nom_ord)
    plt.locator_params(axis='x', nbins=15)
    plt.show()

def courbe_evol_cumul(liste_abs,liste_ord,nom_abs,nom_ord):
    """
    Creating a cumulative 2D plot
    """
    liste_ord = [sum(liste_ord[:i+1]) for i,nb in enumerate(liste_ord)]
    plt.plot(liste_abs, liste_ord)
    plt.xlabel(nom_abs)
    plt.ylabel(nom_ord)
    plt.locator_params(axis='x', nbins=15)
    plt.show()

def pie_chart(labels,sizes,title):
    """
    Creating a pie chart with labels and 'sizes' being the % of space taken
    """
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    fig1, ax1 = plt.subplots()
    ax1.set_title(title, fontsize=14, fontweight='bold')
    fig1.subplots_adjust(top=1.3)

    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def courbe_3d(liste_x,liste_y,liste_z,nom_x,nom_y,nom_z):
    x = np.asarray([float(i) for i in liste_x])
    y = np.asarray([float(i) for i in liste_y])
    z = np.asarray([float(i) for i in liste_z])
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_trisurf(x,y,z, linewidth=0.2, antialiased=True)

    plt.show()







#------------------------------------------------------
# Exemples d'utilisation
#------------------------------------------------------
#
# nb_days = 20
# days = range(nb_days)
# nb_infected = [random.randrange(1, 50, 1) for i in range(nb_days)]
#
# # courbe_evol
# courbe_evol(days,nb_infected,"Jours","Nombre d'infectés")
#
# # courbe_evol_cumul
# courbe_evol_cumul(days,nb_infected,"Jours","Nombre d'infectés")
#
# # pie_chart
# labels = ['65+ ans','45-65 ans','25-45 ans','0-25 ans']
# sizes = [70, 20, 8, 2]
# pie_chart(labels,sizes,'Répartition du nombre d\'infectés en fonction de l\'âge')







# courbe_3d
# nb_days = 20
# days = list(range(nb_days))
# taux = [i/nb_days for i in range(0,3*nb_days,3)] # [0.0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 0.24,...,2.97]
# nb_infected = []
# for t in taux:
#     nb_infected.append(random.randint(int(t*nb_days), int((t*nb_days)**2)))
# courbe_3d(days,taux,nb_infected,'','','')
