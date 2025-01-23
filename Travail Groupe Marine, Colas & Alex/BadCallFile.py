import csv
 
# Affichage de l'entête du programme
print("Tableau de bord")
print('-' * 35)
 
# Ouverture du fichier de données
with open('traiter.csv', encoding='utf-8') as csv_file:
    contenu_csv = csv.reader(csv_file, delimiter=';')
 
    # Stockage des températures pour chaque chambre
    chambres_data = {}
 
    # Lecture des données du fichier
    for row in contenu_csv:
        chambre = row[2]
        try:
            temperature = float(row[3].replace(',', '.'))
            if chambre not in chambres_data:
                chambres_data[chambre] = []
            chambres_data[chambre].append(temperature)
        except ValueError: # Fabrice conseil de tout pété pour savoir qu'elle erreur il y a dans le fichier
            continue
 
# Affichage des résultats
print("                  moy   min   max")
 
for chambre, temperatures in chambres_data.items():
    total = 0
    nombre_temporaire = 0
    minimum = float('inf')
    maximum = float('-inf')
 
    # Trouver Max et Min de chaque chambre
    for temporaire in temperatures:
        if temporaire > maximum:
            maximum = temporaire
        if temporaire < minimum:
            minimum = temporaire
        total += temporaire
        nombre_temporaire += 1
 
    # Affichage des résultats pour chaque chambre
    if nombre_temporaire > 0:
        print(f"{chambre:15} {round(total / nombre_temporaire, 1):5} {minimum:5} {maximum:5}")
 