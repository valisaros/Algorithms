# Suma si media aritmetica a nr. nat

numar_numere = int(input('Dati numarul de numere = '));

suma = 0;
i = 1;

while i <= numar_numere:
    numar = float(input('Dati un numar = '));
    suma += numar;
    i += 1;

print("Suma = " + str(suma));

if  numar_numere != 0:
    media_aritmetica = suma / numar_numere;
    print('Media aritmetica este = ' + str(float(media_aritmetica)));
else:
    print('Nu se poate calcula media aritmetica.');




