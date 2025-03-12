import json

# JSON-bestand lezen
with open(r"c:/xampp/htdocs/BLOK 11/JSON1/data.json") as json_bestand:
    data = json.load(json_bestand)

# Gegevens verwerken
for persoon in data["personen"]:
    print(f"Naam: {persoon['naam']}, Leeftijd: {persoon['leeftijd']}, Stad: {persoon['stad']}, Telefoonnummer: {persoon['telefoonnummer']}")










