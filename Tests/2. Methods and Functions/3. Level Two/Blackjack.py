# Given 3 integers between 1 and 11, if their sum is <= 21 return their sum.
# If their sum exceeds 21 and there's a eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjusment) exceeds 21, return "BUST".

def blackjack(a, b, c):
    suma = a + b + c;

    if suma <= 21:
        return suma

    elif 11 in([a, b, c]) and (suma <= 31):
        return suma - 10

    else:
        return "BUST"
