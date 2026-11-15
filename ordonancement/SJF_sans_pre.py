
nom     = ["P1", "P2", "P3", "P4"]
arrivee = [0, 1, 2, 3]
burst   = [5, 3, 8, 2]

n = len(nom)
fin = [0] * n
fait = [False] * n       # fait[i] = True si le processus i a terminé

t = 0
termines = 0

while termines < n:
    # 1. Parmi les processus arrivés et pas finis, chercher le burst le plus petit
    choisi = -1
    for i in range(n):
        if arrivee[i] <= t and fait[i] == False:
            if choisi == -1 or burst[i] < burst[choisi]:
                choisi = i

    # 2. Personne de prêt : le CPU attend
    if choisi == -1:
        t = t + 1
        continue

    # 3. Le processus choisi s'exécute jusqu'au bout
    t = t + burst[choisi]
    fin[choisi] = t
    fait[choisi] = True
    termines = termines + 1

# Résultats
for i in range(n):
    sejour = fin[i] - arrivee[i]
    attente = sejour - burst[i]
    print(nom[i], "fin =", fin[i], "séjour =", sejour, "attente =", attente)