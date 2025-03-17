def cycle():
    number = int(input("Введите число: "))
    numbers = []
    while number > 0:
        numbers.append(number)
        number -= 1
    print(f"Числа: {numbers}")

    sum = 0
    for num in numbers:
        sum += num
    print(f"Сумма чисел {sum}")

cycle()