# Max dintre n numere

numar_numere = int(input('Dati nr. de numere: '));
numar = int(input('Dati un numar: '));

# Presupunem ca maximul este primul numar introdus.
max = numar;

i = 2;
while i <= numar_numere:
    numar = int(input('Dati un numar: '));  # Noul numar

    # Se compara maximul cu fiecare numar introdus
    if max < numar:
        max = numar;

    i = i + 1;

print('Numarul maxim este: ' + str(max));


