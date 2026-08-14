import datetime
from typing import Tuple, List

# Constantes
TARIFS = {
    "zemidjan": {"base": 150, "km": 75, "majoration": 1.15},
    "taxi": {"base": 200, "km": 100, "majoration": 1.25}
}

# Intervalles d'heure de pointe (convertis en format décimal)
HEURES_DE_POINTE = [
    (7.0, 8.75),  # 07h00 - 08h45
    (11.75, 13.0),  # 11h45 - 13h00
    (17.0, 19.0)  # 17h00 - 19h00
]





# Fonctions Utilitaires
def arrondir_au_multiple(prix: float, multiple: int = 25) -> int:
    """Arrondit le prix final au multiple le plus proche (ex: 25 FCFA)."""
    return round(prix / multiple) * multiple


def est_heure_de_pointe(heure_decimale: float) -> bool:
    """Vérifie si l'heure donnée (en décimal) tombe dans une plage d'heure de pointe."""
    for debut, fin in HEURES_DE_POINTE:
        if debut <= heure_decimale <= fin:
            return True
    return False


def obtenir_heure_decimale(saisie: str) -> Tuple[float, str]:
    """Convertit la saisie (ex: 7h30) en décimal. Utilise l'heure système si vide."""
    if not saisie.strip():
        maintenant = datetime.datetime.now()
        heure_decimale = maintenant.hour + (maintenant.minute / 60.0)
        heure_str = f"{maintenant.hour:02d}h{maintenant.minute:02d}"
        return heure_decimale, heure_str

    try:
        saisie = saisie.lower().replace(':', 'h')
        if 'h' in saisie:
            h, m = saisie.split('h')
            h = int(h)
            m = int(m) if m else 0
            # si la minute dépasse 60
            if m > 60:
                print(" Saisie invalide. Veuillez entrer une minute entre 0 et 59.")
                return -1, ""
            return h + (m / 60.0), f"{h:02d}h{m:02d}"
        else:
            h = float(saisie)
            return h, f"{int(h):02d}h00"
    except ValueError:
        return -1, ""


#  LOGIQUE PRINCIPALE
def afficher_recapitulatif(transport: str, distance: float, heure_str: str, pointe: bool, prix_final: int) -> None:
    """Affiche un ticket récapitulatif créatif et clair."""
    transport_label = "Zemidjan" if transport == "zemidjan" else "Taxi"
    statut_heure = "OUI (Majoration appliquée)" if pointe else "NON (Tarif normal)"

    print("\n" + "=" * 45)
    print(" TICKET DE TRAJET - LOMÉ")
    print("=" * 45)
    print(f" Transport      : {transport_label}")
    print(f" Prix de base     : {TARIFS[transport]['base']} FCFA")
    print(f" Prix au Km     : {TARIFS[transport]['km']} FCFA")            
    print(f" Distance       : {distance:.2f} km")
    print(f" Heure du trajet   : {heure_str}")
    print(f" Heure de pointe: {statut_heure}")
    print("-" * 45)
    print(f" PRIX FINAL     : {prix_final} FCFA")
    print("=" * 45 + "\n")


def main():
    print("Bienvenue dans le Calculateur de Trajet Lomé en (Zemidjan/Taxi) !")
    historique: List[dict] = []

    # Permet à l'utilisateur de calculer plusieurs trajets jusqu'à ce qu'il décide de quitter
    while True:
        # 1. Choix du transport
        transport = input("Moyen de transport ('z' pour Zemidjan, 't' pour Taxi, 'q' pour quitter) : ").strip().lower()

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
            distance = float(input("Distance du trajet (en km) : ").replace(',', '.'))
            if distance <= 0:
                raise ValueError
        except ValueError:
            print(" Distance invalide. Veuillez entrer un nombre positif.")
            continue

        # 3. Heure du trajet
        saisie_heure = input("Heure du trajet (ex: 7h30) [Laissez vide pour l'heure actuelle] : ")
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
    print("\n Merci d'avoir utilisé notre calculateur. À bientôt !")


if __name__ == "__main__":
    main()