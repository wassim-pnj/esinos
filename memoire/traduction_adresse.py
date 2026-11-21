

taille_page = 100
table = [5, 2, 7, 0, -1]        # table[page] = cadre ; -1 = page pas en RAM
adresses = [75, 210, 399, 450]  # adresses logiques demandées

for i in range(len(adresses)):
    adresse = adresses[i]

    page = adresse // taille_page        # numéro de page
    decalage = adresse % taille_page     # position dans la page
    cadre = table[page]                  # on lit la table des pages

    if cadre == -1:
        print("Adresse", adresse, "-> page", page, "-> DÉFAUT DE PAGE")
    else:
        physique = cadre * taille_page + decalage
        print("Adresse", adresse, "-> page", page, "décalage", decalage,"-> cadre", cadre, "-> adresse physique", physique)