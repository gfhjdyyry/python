print("привет")
while True:
    try:
        z = int(input("Пожалуйстп,введите время: "))
        if z >= 5 and z <= 12:
            print("Доброе утро")
        elif z >= 13 and z <= 17:
            print("Добрый день")
        elif z >= 17 and z <= 21:
            print("Добрый Вечер")
        elif z >= 22 and z <= 23:
            print("Доброй ночи")
    except ValueError:
        print("Пожалуйста, введите число")




