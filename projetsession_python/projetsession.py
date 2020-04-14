import matplotlib.pyplot as plt, pandas as pd

#Variable contenant le chemin vers les fichiers .csv contenant les données climatiques
filepath = "historique_sherbrooke.csv"

fields = ["Date/Heure","Mois", "Temp max.(°C)", "Temp min.(°C)", "Temp moy.(°C)", "Pluie tot. (mm)", "Neige tot. (cm)"]

#On lis les fichiers .csv à l'aide de la librairie pandas

csv = pd.read_csv(filepath, usecols=fields)



def calculate_mean(csv, start_date,end_date, data):
    results = []

    datayear = (csv['Date/Heure'] > start_date) & (csv['Date/Heure'] <= end_date)
    somme = csv.loc[datayear].sum()
    sommeTempMax = somme[data]
    mean = sommeTempMax/4
    
    return mean

def print_plot(x, y, ylabel, title):
    plt.plot(x, y)
    plt.xlabel("Année")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

csv = csv.drop(csv[(csv.Mois == 4) | (csv.Mois == 5) | (csv.Mois == 6)| (csv.Mois == 7)| (csv.Mois == 8) | (csv.Mois == 9) | (csv.Mois == 10) | (csv.Mois == 11)].index)
#https://stackoverflow.com/questions/13851535/delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression-involving
#print(csv)

temp_max = "Temp max.(°C)"
snow_total = "Neige tot. (cm)"
rain_total = "Pluie tot. (mm)"

resultsTemp = []
resultsSnow = []
resultsRain = []
x = []

year = 1903

for i in range(68):
    x.append(year)

    start_date = str(year) + "-00"
    end_date = str(year) + "-12"
    meanTemp = calculate_mean(csv, start_date, end_date,temp_max)
    meanSnow = calculate_mean(csv, start_date, end_date,snow_total)
    meanRain = calculate_mean(csv, start_date, end_date,rain_total)
    
    resultsTemp.append(meanTemp)
    resultsSnow.append(meanSnow)
    resultsRain.append(meanRain)
    year += 1

#print_plot(x,resultsSnow, "test", "titre")
print_plot(x,resultsRain, "test", "titre")


