# Write a funcion to check whether a string is a pangram or not
# Note: Pangram = contains every letter of the alphabet

import string

def pangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
