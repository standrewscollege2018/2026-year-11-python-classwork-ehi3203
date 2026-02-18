'''Fizzbuzz game'''

for i in range (1,31):
    #Check if it is divisble by 3. If so, print Fizz
    if NUMBER % 3 == 0:
        print("Fizz")
    elif NUMBER % 5 == 0:
        print("Buzz")
    else:
        print(NUMBER)
    