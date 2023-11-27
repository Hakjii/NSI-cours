from random import randint
tab_perso = []
with open("Characters.csv", mode = 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    key_line = lines[0].strip()
    keys = key_line.split(";")
    for line in lines[1:]:
        line = line.strip()
        values = line.split(";")
        dico = {}
        for i in range(len(keys)):
            dico[keys[i]] = values[i]
        tab_perso.append(dico)
print(tab_perso)

# tri sélection
tab = [randint(1, 25) for i in range(4)]
print(tab)
for i in range(len(tab) - 1):
    indice_min = i
    for j in range(i + 1, len(tab)):
        if tab[j] < tab[indice_min]:
            indice_min = j
    tab[i], tab[indice_min] = tab[indice_min], tab[i]
print(tab)

# tri insertion
for i in range(1, len(tab)):
    temp = tab[i]
    indice = i - 1
    while temp < tab[indice] and i >= 0:
        tab[indice + 1] = tab[indice]
        indice = indice - 1
    tab[indice + 1] = temp

print(tab)