# Programul calculeaza x la puterea n

x = float(input('Dati numarul: '))
n = int(input('Dati puterea: '))

p = 1
i = 1

while i <= n:
    p = p * x;
    i = i + 1;

if n >= 0:
   print('Rezultatul este: ' + str(p))
else:
    p = 1 / p;
    print('Rezultatul este: ' + str(p))

