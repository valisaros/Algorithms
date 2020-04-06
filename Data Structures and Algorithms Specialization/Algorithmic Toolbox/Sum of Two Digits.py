# We make a function for sum

def sum(first_digit, second_digit):
    return (first_digit + second_digit)

# Taking two inputs at a time
A, B = map(int, input().split())
print(sum(A, B))