from function1 import greet
from function2 import calculate_square

name = input("Enter your name: ")
greet(name)

number = int(input("Enter a number: "))
squared_number = calculate_square(number)
print(f"The square of {number} is {squared_number}")