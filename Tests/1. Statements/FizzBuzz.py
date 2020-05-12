# For multiples of 3 print 'Fizz' and for the multiples of 5 print 'Buzz'
# For numbers which are multiples of both print 'FizzBuzz'

for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
