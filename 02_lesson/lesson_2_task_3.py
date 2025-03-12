import math

def square(side):
    return math.ceil(side*side)

side = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата равна {square(side)}")