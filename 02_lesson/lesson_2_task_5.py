def month_to_season(m):
    if m in [1, 2, 12]:
        print("Зима")
    elif m in [3, 4, 5]:
        print("Весна")
    elif m in [6, 7, 8]:
        print("Лето")
    elif m in [9, 10, 11]:
        print("Осень")
    else: 
        print("Неверный номер месяца")

m = int(input("Введите номер месяца(1-12): "))

month_to_season(m)