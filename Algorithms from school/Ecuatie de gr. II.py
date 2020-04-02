# Ecuatie de gradul II
import math
# A, B, C reprezinta numerele
A = float(input('A = '));
B = float(input('B = '));
C = float(input('C = '));

if A != 0:
    print('Exista ecuatie de gradul II');
    delta = B ** 2 - 4 * A * C;
    if delta >= 0:
        print('Exista solutii reale ')
        x1 = (-B) / (2 * A) - math.sqrt(delta) / (2 * A);
        x2 = (-B) / (2 * A) + math.sqrt(delta) / (2 * A);
        print('X1 = ' + str(x1) + ', X2 = ' + str(x2))
    else:
        print('Exista solutii complexe ')
        Re = (-B) / (2 * A);
        Im = math.sqrt(-delta) / (2 * A)
        print('x1 = ' + str(Re) + '-i*' + str(Im))
        print('x2 = ' + str(Re) + '+i*' + str(Im))
else:
    print('Exista ecuatie de gradul II degenerata')
    if B != 0:
        print('Exista ecuatie de gradul I')
        x = (-C)/B;
        print('X = ' + str(x))
    else:
        print('Exisyta ecuatie de gradul I degenerata')
        if C == 0:
            print('Identitate')
        else:
            print('Nonsens');

