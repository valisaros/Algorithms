# Write a function that takes a list and returns a new one with unique elements of the first list

def unique_lst(lst)
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x