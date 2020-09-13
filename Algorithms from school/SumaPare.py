# Suma Pare

n = int(input('Dati numarul de numere: '))
S = 0;
i = 2;
while  (i <= n):
    if ((i % 2) == 0):
         S += i;
    i += 1;
print('Suma numerelor pare este: ' + str(S))