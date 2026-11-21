

nom     = ["P1", "P2", "P3", "P4"]
arrivee = [0, 1, 2, 3]
burst   = [5, 3, 8, 2]

n = len(nom)
fin = [0] * n
t = 0

for i in range(n):
    # Si le CPU est libre avant son arrivée, il attend
    # puisque ils ont deja trie dans l'ordre d'arrivée on passe directement au premier
    if t < arrivee[i]:
        t = arrivee[i]
    # on l'exécute jusqu'au bout
    t = t + burst[i]

    fin[i] = t

# Résultats
for i in range(n):
    sejour = fin[i] - arrivee[i]
    attente = sejour - burst[i]
    print(nom[i], "fin =", fin[i], "séjour =", sejour, "attente =", attente)
