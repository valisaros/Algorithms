'''Fie r un număr real citit de la tastatură, care reprezintă lungimea razei unui cerc.
 Să se scrie un program care să calculeze și să afișeze aria și perimetrul discului de rază r.'''

import math

r = float(input("Introduceti raza cercului: "))

# Calculeaza aria
A = math.pi * (r ** 2)

# Calculeaza perimetrul
P = math.pi * (r * 2)

print(f"Aria cercului este {A}, perimetrul este {P}")