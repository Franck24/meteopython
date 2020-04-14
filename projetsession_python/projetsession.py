import matplotlib.pyplot as plt, pandas as pd

#Variable contenant le chemin vers les fichiers .csv contenant les données climatiques
filepath = "historique_sherbrooke.csv"

fields = ["Date/Heure","Mois", "Temp max.(°C)", "Temp min.(°C)", "Temp moy.(°C)", "Pluie tot. (mm)", "Neige tot. (cm)"]

#On lis les fichiers .csv à l'aide de la librairie pandas

csv = pd.read_csv(filepath, usecols=fields)



def calculate_mean(csv, start_date,end_date):
    results = []

    datayear = (csv['Date/Heure'] > start_date) & (csv['Date/Heure'] <= end_date)
    somme = csv.loc[datayear].sum()
    sommeTempMax = somme["Temp max.(°C)"]
    mean = sommeTempMax/4
    
    return mean



csv = csv.drop(csv[(csv.Mois == 4) | (csv.Mois == 5) | (csv.Mois == 6)| (csv.Mois == 7)| (csv.Mois == 8) | (csv.Mois == 9) | (csv.Mois == 10) | (csv.Mois == 11)].index)
#https://stackoverflow.com/questions/13851535/delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression-involving
#print(csv)


results = []
x = []

year = 1903

for i in range(68):
    x.append(year)

    start_date = str(year) + "-00"
    end_date = str(year) + "-12"
    mean = calculate_mean(csv, start_date, end_date )
    results.append(mean)
    year += 1


plt.plot(x,results)
plt.xlabel("Année")
plt.ylabel("Températures maximales moyennes")
plt.title("YESSIR")
plt.show()



#print(results)