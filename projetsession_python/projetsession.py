import matplotlib.pyplot as plt, pandas as pd

#Variable contenant le chemin vers les fichiers .csv contenant les données climatiques
filepath = "historique_sherbrooke.csv"

fields = ["Date/Heure", "Temp max.(°C)", "Temp min.(°C)", "Temp moy.(°C)", "Pluie tot. (mm)", "Neige tot. (cm)"]

#On lis les fichiers .csv à l'aide de la librairie pandas

csv = pd.read_csv(filepath, usecols=fields)



#print(earlycsv.head())

Total = csv["Pluie tot. (mm)"].sum()


print(csv)

x=csv["Neige tot. (cm)"]
y=csv["Temp moy.(°C)"]


plt.plot(x,y)
plt.xlabel("Total neige")
plt.ylabel("Température")
plt.title("Gros graphique")

#plt.show()