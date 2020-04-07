'''Se citesc două numere a și b reprezentând lungimile laturilor unui dreptunghi.
 Pentru dreptunghiul dat, să se calculeze: perimetrul P, aria A și pătratul lungimii diagonalei D.'''

a, b = [int(x) for x in input("Introdu laturile dreptunghiului: ").split()]

# Calculeaza perimetrul
P = 2 * (a + b)

# Calculeaza aria
A = a * b

# Calculeaza patratul diagonala
D = a * a + b * b


print(f"Perimetrul este {P}, aria este {A} iar patratul diagonalei {D}")