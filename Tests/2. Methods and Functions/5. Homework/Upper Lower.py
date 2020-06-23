# Write a function that accepts a string and calculate the number of upper case letters and lower case letters.

def up_low(s):
    d = {"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original string: ", s)
    print("No. of upper case letters: ", d["upper"])
    print("No. of lower case letters: ", d["lower"])

