n = int(input("Введите число: "))

def fizz_buzz(n):
    for f in range(1, n + 1):
        if f % 3 == 0 and f % 5 == 0:
            print("FizzBuzz")
        elif f % 5 == 0:
            print("Buzz")
        elif f % 3 == 0: 
            print("Fizz")
        else:
            print(f)

fizz_buzz(n)