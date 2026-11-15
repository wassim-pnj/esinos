
nom      = ["P1", "P2", "P3", "P4"]
arrivee  = [0, 1, 2, 3]
burst    = [4, 3, 2, 1]
priorite = [3, 1, 4, 2]

n = len(nom)
restant = list(burst)    # ce qu'il reste à exécuter
fin = [0] * n

t = 0
termines = 0

while termines < n:
    # 1. Parmi les processus arrivés et pas finis, chercher la meilleure priorité
    choisi = -1
    for i in range(n):
        if arrivee[i] <= t and restant[i] > 0:
            if choisi == -1 or priorite[i] < priorite[choisi]:
                choisi = i

    # 2. Personne de prêt : le CPU attend
    if choisi == -1:
        t = t + 1
        continue

    # 3. Le processus choisi s'exécute UNE seule unité de temps
    t = t + 1
    restant[choisi] = restant[choisi] - 1

    # 4. S'il a fini, on note sa fin
    if restant[choisi] == 0:
        fin[choisi] = t
        termines = termines + 1

# Résultats
for i in range(n):
    sejour = fin[i] - arrivee[i]
    attente = sejour - burst[i]
    print(nom[i], "fin =", fin[i], "séjour =", sejour, "attente =", attente)