# step 1. Ask for 3 numbers
import math
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

math.floor(number1, number2, number3)

# Find the lowest among three numbers
# number1 is the lowest number
if number1 < number2 and number2 < number3:
    print("The lowest number is number1")
else:
    # number2 as the lowest number
    if number2 < number1 and number1 < number3:
        print("The lowest number is number2")
    else:
        # number3 as the lowest number
        if number3 < number2 and number2 < number1:
            print("The lowest number is number3")

print("DONE!")
    



