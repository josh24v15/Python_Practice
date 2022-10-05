"""Write a function named collatz() with one parameter named number.
If even, collatz prints number // 2 and returns this value
If odd, print and return 3 * number + 1.
Then write a program that, when given an integer, collatz() is called until it returns a value of 1.
BONUS: add try and except statements to detect whether input is a noninteger string.
"""
def collatz(number):
    if number == 1:
        return 1
    elif number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return (3 * number + 1)

integer = ''
while not integer:
    try:
        integer = int(input("Please enter an integer: "))
    except:
        print("That is not an integer!")
while integer != 1:
    integer = collatz(integer)