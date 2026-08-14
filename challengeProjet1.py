import datetime
from calculateur import *

#  LOGIQUE PRINCIPALE

def main():
    print("Bienvenue dans le Calculateur de Trajet Lomé en (Zemidjan/Taxi) !")
    historique: List[dict] = []

    # Permet à l'utilisateur de calculer plusieurs trajets jusqu'à ce qu'il décide de quitter
    while True:
        # 1. Choix du transport
        transport = input("Choisissez votre moyen de transport ('z' pour Zemidjan, 't' pour Taxi, 'q' pour quitter) : ").strip().lower()

        if transport == 'q':
            break
        elif transport in ['z', 'zemidjan']:
            choix_transport = "zemidjan"
        elif transport in ['t', 'taxi']:
            choix_transport = "taxi"
        else:
            print(" Saisie invalide. Veuillez choisir 'z' ou 't'.")
            continue

        # 2. Distance
        try:
            distance = float(input(" Entrez la distance du trajet (en km) : ").replace(',', '.'))
            if distance <= 0:
                raise ValueError
        except ValueError:
            print(" Distance invalide. Veuillez entrer un nombre positif.")
            continue

        # 3. Heure du trajet
        saisie_heure = input("Entrez l'heure du trajet (ex: 7h30) [Laissez vide pour l'heure actuelle] : ")
        heure_decimale, heure_str = obtenir_heure_decimale(saisie_heure)

        if heure_decimale < 0 or heure_decimale > 23:
            print(" Format d'heure invalide. Utilisez le format HHhMM.")
            continue

        # 4. Calculs
        tarif = TARIFS[choix_transport]
        prix_base = tarif["base"] + (tarif["km"] * distance)

        pointe = est_heure_de_pointe(heure_decimale)
        if pointe:
            prix_total = prix_base * tarif["majoration"]
        else:
            prix_total = prix_base

        # Arrondi au multiple de 25
        prix_final = arrondir_au_multiple(prix_total, 25)

        # 5. Affichage
        afficher_recapitulatif(choix_transport, distance, heure_str, pointe, prix_final)

        # Historique
        historique.append({
            "transport": choix_transport,
            "distance": distance,
            "heure": heure_str,
            "prix": prix_final
        })

    # Fin du programme
    print("\n HISTORIQUE DE LA SESSION :")
    if not historique:
        print("Aucun trajet calculé.")
    else:
        for i, trajet in enumerate(historique, 1):
            print(
                f"  {i}. {trajet['transport']} | {trajet['distance']} km | {trajet['heure']} -> {trajet['prix']} FCFA")
    print("\n Merci d'avoir utilisé notre calculateur. À bientôt sur la route !")


