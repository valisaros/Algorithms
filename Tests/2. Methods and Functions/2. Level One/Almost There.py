# Goven an integer n, return True if n is within 10 of either 100 and 200

def almost_there(n):

    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)