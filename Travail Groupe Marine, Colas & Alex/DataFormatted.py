# Code source exercice 3
 
# affichage des temperatures v1
import csv
 
# Affichage de l'entete du programme
print("Tableau de bord")
print('-'*57)
   
# Ouverture du fichier de données
with open('traiteur.csv') as csv_file:
    contenu_csv = csv.reader(csv_file, delimiter=';')
   
   
print("               ", "moy", "min", "max")
 
for chambre in ["chambrefroide01", "chambrefroide02", "chambrefroide03"] :
    total = 0
    nb_temp = 0
    minimum = 15
    maximum = -1
    if chambre == chambre :
        if chambre[3]>maximum :
            maximum = chambre[3]
        if chambre[3]<minimum :
             minimum = chambre[3]
        total = total + chambre[3]
        nb_temp = nb_temp + 1
    print (chambre, round(total / nb_temp, 2), minimum, maximum)