
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
    # 1.parmi les processus arrivés et pas finis, chercher la meilleure priorité
    choisi = -1 #-1: aucun processus choisi
    for i in range(n):
        if arrivee[i] <= t and restant[i] > 0: #processus deja venu et pas encore fini
            if choisi == -1 or priorite[i] < priorite[choisi]: #soit y a aucun processus choisi, soit il a une priorité plus faible
                choisi = i

    # 2.personne de prêt : le cpu attend
    if choisi == -1:
        t = t + 1
        continue           # retoune au début de la boucle while

    # 3. on exécute le processus choisi pendant 1 unité de temps
    t = t + 1
    restant[choisi] = restant[choisi] - 1 # on soustrait 1 du burst restant 

    # 4. S'il a fini, on note sa fin
    if restant[choisi] == 0: 
        fin[choisi] = t
        termines = termines + 1

# Résultats
for i in range(n):
    sejour = fin[i] - arrivee[i]
    attente = sejour - burst[i]
    print(nom[i], "fin =", fin[i], "séjour =", sejour, "attente =", attente)