from calculator import operation, get_number, calc

def run():
    oper = operation()
    if not oper:
        return
    x = get_number("Введите первое число: ")
    y = get_number("Введите второе число: ")
    result = calc(x, y, oper)
    print(f"Результат: {result}")

if __name__ == "__main__":
    while True:
        run()
        cont = input("Хотите выполнить ещё вычисление? (да/нет): ").strip().lower()
        if cont != 'да':
            print("Выход из программы.")
            break
