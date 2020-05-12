# Use for, split() and if to create a Statement that will print out words that start with 's'.

st = "Print only the words that start with s in this sentence"

words = st.split()

for word in words:
    if word[0] == 's':
        print(word)