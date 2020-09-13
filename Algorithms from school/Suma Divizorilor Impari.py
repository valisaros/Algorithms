# Suma Divizorilor Impari

n = int(input('Dati numarul: '))
NRDIV = 0;
i = 1;
divizor = 1;
while i <= n:
    if ((n % divizor) == 0) and ((divizor % 2) != 0):
        NRDIV += divizor;
    i += 1;
    divizor += 1;
print('Suma divizorilor impari ai numarului ' + str(n) + ' este ' + str(NRDIV))
