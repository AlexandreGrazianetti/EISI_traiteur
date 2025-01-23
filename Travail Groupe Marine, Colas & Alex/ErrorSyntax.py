# affichage des temperatures v1
import csv

# Affichage de l'entete du programme
print("Affichage des mesures de température d'une chambre froide")
print('-'*57)

# Selection d'une chambre froide
num_chambrefroide = input('Choisissez un numéro de chambre froide (1, 2 ou 3) : ')

if num_chambrefroide in ('1','2','3'):
    # Nom de la chambre froide a rechercher dans les données
    recherche = 'chambrefroide0' + num_chambrefroide
    
    # Ouverture du fichier de données
    with open('traiteur_ErrorSyntax.csv') as csv_file:
        contenu_csv = csv.reader(csv_file, delimiter=';')
        
        # parcours des données du fichier
        for champ in contenu_csv:
            if champ[2] == recherche:
                print(champ[0],champ[1],champ[2],champ[3])
else:
    print("erreur: numéro de chambre froide incorrect")