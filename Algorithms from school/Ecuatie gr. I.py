# Ecuatie de gradul I

# A,B reprezinta numerele
A = float(input('Dati A = '));
B = float(input('Dati B = '));

if A != 0:
    print ('Exista ecuatie de gr. I ')
    x = -B/A;
    print ('X = ' + str(x))
else:
    if B == 0:
        print('Identitate')
    else:
        print('Nonsens')
