import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from scipy import stats
import random
import numpy as np




def courbe_evol(liste_abs,liste_ord,nom_abs,nom_ord):
    plt.plot(liste_abs, liste_ord)
    plt.xlabel(nom_abs)
    plt.ylabel(nom_ord)
    plt.locator_params(axis='x', nbins=15)
    plt.show()

def courbe_evol_cumul(liste_abs,liste_ord,nom_abs,nom_ord):
    liste_ord = [sum(liste_ord[:i+1]) for i,nb in enumerate(liste_ord)]
    plt.plot(liste_abs, liste_ord)
    plt.xlabel(nom_abs)
    plt.ylabel(nom_ord)
    plt.locator_params(axis='x', nbins=15)
    plt.show()

def pie_chart(labels,sizes,title):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    fig1, ax1 = plt.subplots()
    ax1.set_title(title, fontsize=14, fontweight='bold')
    fig1.subplots_adjust(top=1.3)

    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def courbe_3d(liste_x,liste_y,_liste_z,nom_x,nom_y,nom_z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()







#------------------------------------------------------
# Exemples d'utilisation
#------------------------------------------------------

nb_days = 20
days = range(nb_days)
nb_infected = [random.randrange(1, 50, 1) for i in range(nb_days)]

# courbe_evol
courbe_evol(days,nb_infected,"Jours","Nombre d'infectés")

# courbe_evol_cumul
courbe_evol_cumul(days,nb_infected,"Jours","Nombre d'infectés")

# pie_chart
labels = ['65+ ans','45-65 ans','25-45 ans','0-25 ans']
sizes = [70, 20, 8, 2]
pie_chart(labels,sizes,'Répartition du nombre d\'infectés en fonction de l\'âge')

# courbe_3d
courbe_3d([],[],[],'','','')
