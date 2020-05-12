# Use List Comprehension to create a list for the first letters of every word in the strig below:

st = "Create a list of the first letters of every word in this string"

lst = [letter[0] for letter in [word for word in st.split()]]
print(lst)