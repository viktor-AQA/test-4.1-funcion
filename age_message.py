from datetime import datetime

def age_calculate():
    try:
        birth_year = int(input("Введите год вашего рождения: "))
        age_count = datetime.now().year - birth_year
        print(f"Ваш возраст: {age_count}")

        if 18 > age_count:
            print("Вы еще молоды, учеба — ваш путь!")
        elif 18 <= age_count < 65:
            print("Отличный возраст для карьерного роста!")
        else:
            print("Пора наслаждаться заслуженным отдыхом!")

    except ValueError:
        print("Пожалуйста, введите корректный год рождения.")

age_calculate()
