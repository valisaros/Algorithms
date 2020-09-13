# suma divizori

n = int(input('Dati numarul: '))
S = 0;
divizor = 1;
i = 1;
while i <= n:
    if (n % divizor) == 0:
        S = S + divizor;
    divizor += 1;
    i += 1;
print('Suma divizorilor este ' + str(S));