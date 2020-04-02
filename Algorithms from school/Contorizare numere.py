# contorizare numere

# Se cere numarul de numere
numar_numere = int(input('Dati numarul de numere: '))

# Se intializeaza cu 0 variabilele care au rol de a contoriza numerele pozitive, negative si nule
pozitive = 0
negative = 0
nule = 0

i = 1
while i <= numar_numere:
    numar = float(input('Dati numarul: '))
    if numar > 0:
        pozitive += 1;
    elif numar < 0:
        negative += 1;
    else:
        nule += 1;
    i = i + 1;                         # obligatoriu

print('Pozitive = ' + str(pozitive))
print('Negative = ' + str(negative))
print('Nule = ' + str(nule))