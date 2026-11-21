
nom     = ["P1", "P2", "P3", "P4"]
arrivee = [0, 1, 2, 3]
burst   = [5, 3, 8, 2]
quantum = 3

n = len(nom)
restant = list(burst) #copie burst dans restant
fin = [0] * n

t = 0
file = []
termines = 0
p = -1          # processus qui vient de s'exécuter (-1 = aucun pour l'instant)

while termines < n:
    # 1. Ajouter dans la file ceux qui sont arrivés
for i in range(n):
        if arrivee[i] <= t and restant[i] > 0 and i not in file and i != p: # processus deja venu, pas fini, pas deja dans la file et pas celui qui vient de s'executer
            file.append(i)

    # 2. Si la file est vide, le CPU attend
    if len(file) == 0:
        t = t + 1
        continue

    # 3. Prendre le premier de la file et l'enlever de la file (il va s'executer)
    p = file.pop(0)

    # 4. Durée d'exécution, burst restant ou quantum, selon le plus petit
    if restant[p] <= quantum:
        duree = restant[p]
    else:
        duree = quantum

    # 5. Le temps avance
    t = t + duree
    restant[p] = restant[p] - duree

    # 6. Ajouter les nouveaux arrivés (ils passent avant p), mais pas ceux qui sont déjà dans la file et pas p lui-même
    for i in range(n):
        if arrivee[i] <= t and restant[i] > 0 and i not in file and i != p:
            file.append(i)

    # 7. Pas fini : p retourne à la fin. Fini : on note sa fin.
    if restant[p] > 0:
        file.append(p)
    else:
        fin[p] = t
        termines = termines + 1

for i in range(n):
    sejour = fin[i] - arrivee[i]
    attente = sejour - burst[i]
    print(nom[i], "fin =", fin[i], "séjour =", sejour, "attente =", attente)