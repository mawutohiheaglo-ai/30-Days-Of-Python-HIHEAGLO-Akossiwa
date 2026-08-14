from constantes import *
import datetime
from typing import Tuple, List



# La fonction pour convertir l'heure saisie

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


# La fonction qui permet de verifier si l'heure saisie correspond à l'heure de pointe


def est_heure_de_pointe(heure_decimale: float) -> bool:
    """Vérifie si l'heure donnée (en décimal) tombe dans une plage d'heure de pointe."""
    for debut, fin in HEURES_DE_POINTE:
        if debut <= heure_decimale <= fin:
            return True
    return False   

def arrondir_au_multiple(prix: float, multiple: int = 25) -> int:
    """Arrondit le prix final au multiple le plus proche (ex: 25 FCFA)."""
    return round(prix / multiple) * multiple

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






