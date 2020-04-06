# Fibonacci

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# introducere nr. termeni

nrtermeni = int(input('Dati numar de termeni: '))

# verificam daca numarul este valid

if nrtermeni <= 0:
   print("Introdu un numar pozitiv intreg")
else:
   print("Fibonacci sir:")
   for i in range(nrtermeni):
       print(recur_fibo(i))



