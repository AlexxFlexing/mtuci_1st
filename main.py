from function1 import greet
from function2 import calculate_square

name = input("Введите ваше имя: ")
greet(name)

number = int(input("Введите число: "))
squared_number = calculate_square(number)
print(f"Квадрат числа {number} это {squared_number}")