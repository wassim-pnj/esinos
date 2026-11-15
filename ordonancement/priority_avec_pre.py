
nom      = ["P1", "P2", "P3", "P4"]
arrivee  = [0, 1, 2, 3]
burst    = [4, 3, 2, 1]
priorite = [3, 1, 4, 2]

n = len(nom)
fin = [0] * n
fait = [False] * n       # fait[i] = devient True si le processus i est termine

t = 0
termines = 0

while termines < n:
    # 1. Parmi les processus arrives et pas finis, chercher la meilleure priorite
    choisi = -1          # -1 = personne choisi pour l'instant
    for i in range(n):
        if arrivee[i] <= t and fait[i] == False:
            if choisi == -1 or priorite[i] < priorite[choisi]:
                choisi = i

    # 2. Personne de pret : le CPU attend
    if choisi == -1:
        t = t + 1
        continue

    #on execute le processus choisi
    t = t + burst[choisi]
    fin[choisi] = t
    fait[choisi] = True
    termines = termines + 1

# on affiche les resultats
for i in range(n):
    sejour = fin[i] - arrivee[i]
    attente = sejour - burst[i]
    print(nom[i], "fin =", fin[i], "sejour =", sejour, "attente =", attente)