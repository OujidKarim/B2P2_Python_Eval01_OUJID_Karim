# Evaluation python data Karim Oujid
import numpy as np
import matplotlib.pyplot as plt

# Exercice 1

# tmin = np.genfromtxt('./data/2016/tmin.csv', delimiter=',')
# tmax = np.genfromtxt('./data/2016/tmax.csv', delimiter=',')
# tmoy = np.genfromtxt('./data/2016/tmoy.csv', delimiter=',')


# Exercice 2

# donnees = np.array([tmax, tmin, tmoy]).T

# Exercice 3

# delta = tmax - tmin
# donnees = np.c_[donnees, delta]

# Exercice 4


# les données de chaque année seront stockées dans un tableau différent (donnees2016, donnees2017, etc...) lui même stocké dans un dictionnaire donnees_dict
donnees_dict = {}
for annee in range(2016, 2023):
    tmin = np.genfromtxt(f'./data/{annee}/tmin.csv', delimiter=',')
    tmax = np.genfromtxt(f'./data/{annee}/tmax.csv', delimiter=',')
    tmoy = np.genfromtxt(f'./data/{annee}/tmoy.csv', delimiter=',')
    
    donnees = np.array([tmax, tmin, tmoy]).T
    
    delta = tmax - tmin
    donnees = np.c_[donnees, delta]
    donnees_dict[f'donnees{annee}'] = donnees

# Exercice 5


for annee, donnees in donnees_dict.items():
    tmax_annee = np.max(donnees[:, 0])
    tmin_chaud = np.min(donnees[donnees[:, 0] == tmax_annee, 1])
    tmoy_annee = np.mean(donnees[:, 2])
    delta_moy = np.mean(donnees[:, 0] - donnees[:, 1])
#   print(f" {annee}  : Tmax = {tmax_annee}, Tmin jour chaud = {tmin_chaud}, Tmoy = {tmoy_annee:.2f}, Delta moy = {delta_moy:.2f}")

# Exercice 6

# Exercice 6

#Stocke les différentes données que l'on veut afficher (qui sont les mêmes que sur l'exo 5)
annees = []
tmax_values = []
tmin_chaud_values = []
tmoy_values = []
delta_moy_values = []

# boucle pour chaque année qui calcule:
# - la température max
# - la température min du jour le plus chaud
# - la température moyenne sur l'année
# - la température moyenne des écarts
for annee, donnees in donnees_dict.items():
    annees.append(int(annee.replace('donnees', '')))
    tmax_annee = np.max(donnees[:, 0])
    tmin_chaud = np.min(donnees[donnees[:, 0] == tmax_annee, 1])
    tmoy_annee = np.mean(donnees[:, 2])
    delta_moy = np.mean(donnees[:, 0] - donnees[:, 1])

    tmax_values.append(tmax_annee)
    tmin_chaud_values.append(tmin_chaud)
    tmoy_values.append(tmoy_annee)
    delta_moy_values.append(delta_moy)

#Crée un graphique avec les 4 courbes. 
plt.figure(figsize=(10, 6))
plt.plot(annees, tmax_values, marker='.', label="Température maximale")
plt.plot(annees, tmin_chaud_values, marker='.', label="Température minimale du jour le plus chaud de l'année")
plt.plot(annees, tmoy_values, marker='.', label="Température moyenne sur l'année")
plt.plot(annees, delta_moy_values, marker='.', label="Température moy des écarts")

#Les éléments affichés sur le graphique pour une meilleure compréhension (titre, nom ordonnées, nom abscisses, etc... )
plt.xlabel("Année")
plt.ylabel("Température (°C)")
plt.title("Évolution des températures sur ces 7 dernières années")
plt.legend()
plt.grid(True)
plt.show()

# Exercice 7

# Pour le température maximale, on voit qu'elle augmente soudainement à partir de 2017, qu'elle atteint son pic en 2019 et puis qu'elle redescend jusqu'à 2021. En 2022 on atteint le même pic que 2019. La température max est très irrégulière.
# Pour la température minimum du jour le plus chaud de l'année, globalement elle n'évolue quasiment pas et stagne autour de 20°.
# Pour la température moyenne sur l'année, elle stagne également entre 10 et 15°, bien que l'on peut voir un léger pic en 2022 se rapprochant de 20°. La température moyenne est plutôt basse comparée à la température maximale.
# Pour La température moyenne des écarts, elle est globalement très basse et stagne autour de 5-10°, le pic le plus bas étant en 2017 avec environ 4°. 

