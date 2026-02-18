
print("Enter two numbers")
number1 = int(input("number1"))
get_num = True
while get_num == True:
    number2 = int(input("number2"))
    if number1<number2:
        get_num = False
    elif number1>number2:
        print("Incorret")
print("Correct")
print(f"{number1}")