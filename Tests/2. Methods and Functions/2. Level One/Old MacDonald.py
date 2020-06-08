# Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):

    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()


    '''First_letter = name[0]
    Inbetween = name[1:3]
    Fourth_letter = name[3]
    rest = name[4:]

    return First_letter.upper() + Inbetween + Fourth_letter.upper() + rest'''


