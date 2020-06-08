# Write a function that takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):

    wordlist = text.split()

    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0]