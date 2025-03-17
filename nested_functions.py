def calculator():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *, /): ")
    if "+" in operation:
        print(f"Cумма чисел равна: {a + b}")
    elif "-" in operation:
        print(f"Разность чисел равна: {a - b}")
    elif "*" in operation:
        print(f"Произведение чисел равно: {a * b}")
    else:
        print(f"Частное чисел равно: {a / b}")

calculator()