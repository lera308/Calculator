def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def operation():
    oper = input("Выберите операцию (+, -, *, /): ").strip()
    if oper in ['+', '-', '*', '/']:
        return oper
    else:
        print("Неизвестная операция!")
        return None

def calc(x, y, oper):
    if oper == '+':
        return add(x, y)
    elif oper == '-':
        return subtract(x, y)
    elif oper == '*':
        return multiply(x, y)
    elif oper == '/':
        return divide(x, y)
