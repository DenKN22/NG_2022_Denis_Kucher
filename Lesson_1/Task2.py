import math
operation =  input("Write you operation (+,-,/,*,sqr,sqrt): ")
print("if you choose sqr or sqrt write only first a")
a = int(input("Write a: "))
b = int(input("Write b: "))

if operation == '+':
    print("You answer ",a+b)
if operation == '-':
    print("You answer ",a-b)
if operation == '/':
    print("You answer ",a/b)
if operation == '*':
    print("You answer ",a*b)
if operation == 'квадрат':
    print("Ваша відповідь ",a**2)
if operation == 'корінь':
    print("You answer ",math.sqrt(a))
