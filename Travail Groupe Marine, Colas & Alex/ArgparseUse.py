import csv
from collections import defaultdict
import argparse


def afficher_entete():
    print("Tableau de bord")
    print('-' * 57)
    print(f'{"Chambre":<13} {"Moy":>7} {"Min":>5} {"Max":>5}')


def traiter_ligne(champ, chambres_froides):
    if len(champ) < 4:
        return  # Ligne incomplète, on ignore

    chambre = champ[2].strip()
    temperature_str = champ[3].strip()

    if not chambre or not temperature_str:
        return  # Si une donnée clé est vide, on ignore

    try:
        temperature = float(temperature_str.replace(',', '.'))
        data = chambres_froides[chambre]
        data['sum'] += temperature
        data['count'] += 1
        data['min'] = min(data['min'], temperature)
        data['max'] = max(data['max'], temperature)
    except ValueError:
        pass  # Ignorer les températures non valides


def calcul_et_affichage(chambres_froides):
    for chambre, data in chambres_froides.items():
        if data['count'] > 0:
            moyenne = data['sum'] / data['count']
            print(f'{chambre:<15} {moyenne:>5.1f} {data["min"]:>5.1f} {data["max"]:>5.1f}')
        else:
            print(f'{chambre:<15} Aucune donnée disponible')


def main():
    # Utilisation d'argparse pour gérer les arguments
    parser = argparse.ArgumentParser(description="Analyser les données de températures des chambres froides.")
    parser.add_argument("fichier", type=str, help="Chemin du fichier CSV à analyser")

    args = parser.parse_args()
    fichier_csv = args.fichier

    afficher_entete()

    chambres_froides = defaultdict(lambda: {'sum': 0, 'count': 0, 'min': float('inf'), 'max': float('-inf')})

    try:
        with open(fichier_csv) as csv_file:
            for champ in csv.reader(csv_file, delimiter=';'):
                traiter_ligne(champ, chambres_froides)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier_csv}' est introuvable.")
        return

    calcul_et_affichage(chambres_froides)


if __name__ == "__main__":
    main()
