def check_triangle():
    a = int(input("Введите длину первой стороны: "))
    b = int(input("Введите длину первой стороны: "))
    c = int(input("Введите длину первой стороны: "))
    if (a + b) > c and (b + c) > a and (a + c) > b:
        if a == b == c:
            print("Равносторонний треугольник")
        elif a == b or a == c or b == c:
            print("Равнобедренный треугольник")
        else:
            print("Разносторонний треугольник")


check_triangle()