# Write a function that returns the lesser of two given numbers if both are even
# but returns the greater if one or both are numbers are odd

def lesser_of_two_evens(a, b):

    if (a % 2 == 0) and (b % 2 == 0):
        return min(a,b)

    else:
        return max(a,b)
