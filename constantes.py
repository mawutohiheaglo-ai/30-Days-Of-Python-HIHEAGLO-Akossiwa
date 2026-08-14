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


