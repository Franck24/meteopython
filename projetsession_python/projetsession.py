import pandas as pd

#Variable contenant le chemin vers les fichiers .csv contenant les données climatiques
filepath1 = "sherbrooke_1930.csv"
filepath2 = "sherbrooke_1970.csv"

fields = ["Date/Heure", "Temp max.(°C)", "Temp min.(°C)", "Temp moy.(°C)", "Pluie tot. (mm)", "Neige tot. (cm)"]
#On lis les fichiers .csv à l'aide de la librairie pandas

earlycsv = pd.read_csv(filepath1, usecols=fields)
latercsv = pd.read_csv(filepath2, usecols=fields)


print(earlycsv.head())



