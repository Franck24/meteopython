#Importation des modules nécessaires au fonctionnement du programme
import matplotlib.pyplot as plt, pandas as pd, os, sys, tkinter, numpy
from tkinter.filedialog import askopenfilename


#Variable contenant le chemin par défaut vers le fichier .csv contenant les données climatiques
filepath = "..historique_sherbrooke.csv"


#Variable qui sert à spécifier les champs du fichier qu'on veut lire uniquement
fields = ["Date/Heure","Mois", "Temp max.(°C)", "Temp min.(°C)", "Temp moy.(°C)", "Pluie tot. (mm)", "Neige tot. (cm)"]


#Fonction qui vérifie si l'emplacement et le fichier sont valides
def validatefile(filepath):

    validfile = False
    
    while validfile !=True:
        stop = False
        try:
            csv = pd.read_csv(filepath, usecols=fields) #Le chemin du fichier est valide, on retourne le fichier
            return csv
        except FileNotFoundError:
            clearconsole()
            print("Fichier introuvable. Chercher manuellement le fichier historique_sherbrooke.csv")
            filepath = browsefile()
            validfile = False #On refait la boucle pour tester à nouveau le chemin
        except ValueError:    #L'utilisateur n'a pas ouvert le bon fichier, on lui demande d'ouvrir à nouveau le fichier ou de quitter
            clearconsole()
            userchoice = input("Vous n'avez pas ouvert le bon fichier. Entrez 1 pour réessayer ou q pour quitter\n>")
            while stop == False:
                if userchoice.lower() == "q": 
                    sys.exit("Au revoir!") 
                elif userchoice == "1":   
                    filepath = browsefile()
                    validfile = False
                    stop=True


#Fonction permettant à l'utilisateur d'aller chercher le fichier manuellement sur son ordinateur
def browsefile():

    tkwindow = tkinter.Tk()      #Assigne la fenêtre à une variable
    filepath = askopenfilename() #Ouvre un explorateur de fichier pour sélectionner le fichier
    tkwindow.destroy()           #On détruit la variable contenant la fenêtre, sinon une fenêtre blanche reste ouverte

    return filepath


#Fonction qui supprime le texte de la console ou terminal
def clearconsole():

    if sys.platform.startswith('linux') or sys.platform.startswith('darwin') : #test si le système d'exploitation est Linux ou MacOS, si oui on supprime l'affichage
        os.system('clear') 
    elif sys.platform.startswith('win32'): #sinon on vérifie si le système d'exploitation est Windows, si oui on supprime l'affichage
        os.system('cls')


#Fonction servant à calculer la moyenne des données passées en paramètres
def calculate_mean(csv, start_date,end_date, data):
  
    datayear = (csv['Date/Heure'] > start_date) & (csv['Date/Heure'] <= end_date)   #On prend les données entre deux années spécifiques
    cellsum = csv.loc[datayear].sum()  #On fait la somme des cellules 
    total = cellsum[data]       #On prend seulement la somme de la colonne spécifiées avec la variable "data"
    mean = total/4              #On calcul la moyenne
    
    return mean


#Fonction qui affiche les différents graphiques
def print_plot(x, y, ylabel, title):
   
   #Création du graphique à lignes brisées de base
    plt.plot(x,y)       #Trace le graphique avec les variables en x (années) et en y (température max, qté neige, qté pluie)
    plt.xlabel("Année") #On attribut une étiquette à l'axe des x 
    plt.ylabel(ylabel)  #On attribut une étiquette à l'axe des y
    plt.title(title)    #On entre le titre du graphique

   #Calcul de la droite de tendance
    z = numpy.polyfit(x,y,1) #La fonction polyfit effectue le calcul des moindres carrés
    f = numpy.poly1d(z)
    plt.plot(x,f(x),"r-")    #Trace la droite de tendance en rouge ("r-")

    plt.show()               #On affiche le graphique à l'utilisateur



#On appel la fonction pour vérifier le chemin du fichier
csv = validatefile(filepath) 


#On supprime toutes les rangées qui contient des mois en dehors de la saison d'hiver. On conserve Janvier, Février, Mars et Décembre
csv = csv.drop(csv[(csv.Mois == 4) | (csv.Mois == 5) | (csv.Mois == 6)|
(csv.Mois == 7)| (csv.Mois == 8) | (csv.Mois == 9) | (csv.Mois == 10) | (csv.Mois == 11)].index)

#Variables contenant le nom des colonnes qui serviront aux calculs des moyennes
temp_max = "Temp max.(°C)"
snow_total = "Neige tot. (cm)"
rain_total = "Pluie tot. (mm)"

#Variables qui contiendront les moyennes de chaque années
resultsTemp = []
resultsSnow = []
resultsRain = []
#Variable qui contiendra les années pour chaque moyennes
x = []

year = 1903 #L'année où l'on commence les calculs

stop = False

for i in range(68):

    x.append(year) #Ajoute l'année du calcul en cours

    start_date = str(year) + "-00"
    end_date = str(year) + "-12"

    #Appel les fonctions pour calculer chaque moyennes
    meanTemp = calculate_mean(csv, start_date, end_date,temp_max)
    meanSnow = calculate_mean(csv, start_date, end_date,snow_total)
    meanRain = calculate_mean(csv, start_date, end_date,rain_total)
    
    #Ajoute les résultats des moyennes dans leurs variables respectives
    resultsTemp.append(meanTemp)
    resultsSnow.append(meanSnow)
    resultsRain.append(meanRain)

    year += 1

while stop == False :

    clearconsole() #Supprime l'affichage des la console ou terminal

    userchoice = input("Entrez le numéro du graphique que vous désirez obtenir.\n\n 1  Température moyenne maximale par année\n 2  Précipitations de neige moyenne par année\n 3  Précipitations de pluie moyenne par année\n q  Quitter\n\n>")

    if userchoice.lower() == "q": #si l'utilisateur tape "q" on quitte le programme
        print("Au revoir!")
        stop = True
    #Sinon on affiche le graphique demandé par l'utilisateur 
    elif userchoice == "1":
        print_plot(x,resultsTemp,"Température en °C", "Température moyenne maximale pendant la saison d'hiver\n à Sherbrooke pour la période de 1903 à 1970")
    elif userchoice == "2":
        print_plot(x,resultsSnow, "Quantité de neige totale (cm)", "Quantité de neige moyenne tombée pendant la saison d'hiver\n à Sherbrooke pour la période de 1903 à 1970")
    elif userchoice == "3":
        print_plot(x,resultsRain, "Quantité de neige totale (mm)", "Quantité de pluie moyenne tombée pendant la saison d'hiver\n à Sherbrooke pour la période de 1903 à 1970")