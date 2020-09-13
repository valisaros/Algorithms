# Suma Gauss

n = int(input('Dati numarul: '))
S = 0;
i = 1;
while i <= n:
    S += i;
    i += 1;
print('Suma numerelor de la 0 pana la ' + str(n) + ' este ' + str(S));
