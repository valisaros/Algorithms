# Euclid

# A, B reprezinta numerele
A = int(input('Dati A = '))
B = int(input('Dati B = '))

# Daca A < B se face interschimbarea pentru ca A > B prin intermediul variabilei auxiliare "aux"
if A < B:
    aux = A;
    A = B;
    B = aux;

# R reprezinta restul
R = A % B;
while R != 0:
    A = B;
    B = R;
    R = A % B;
print('Cmmdc= ' + str(B));          #cmmdc = cel mai mic divizor comun
