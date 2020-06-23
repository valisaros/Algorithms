# Write a fucntion that checks whether a number is in a given range (inclusive of high and low)

def range_check(num,high,low):
    if num in range(low,high):
        print (f"{num} is in the range")
    else:
        print("The number is outside the range")

