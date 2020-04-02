# Numere prime

numar = int(input('Dati numarul: '))

NRDIV = 0;
divizor = 1;

while divizor <= numar:
    if (numar % divizor) == 0:
        NRDIV = NRDIV + 1;

    divizor = divizor + 1;

if NRDIV <= 2:
    print('Numarul ' + str(numar) + ' este prim.' )
else:
    print('Numarul ' + str(numar) + ' nu este prim.')
