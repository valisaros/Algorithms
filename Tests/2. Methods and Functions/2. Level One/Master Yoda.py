# Given a sentence, return a sentence with the words reversed

def reversed_words(text):
    words = text.split()
    reversed = words[::-1]

    return ' '.join(reversed)
print(reversed_words("My name is"))