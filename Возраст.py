print("Здравствуй, дорогой игрок!Вы будете играть в игру 'Возраст'")
while True:
    try:
        age = int(input("Пожалуйста, введите возраст: "))
        if age >= 1 and age <= 12:
          print("Детство")
        elif age >= 13 and age <= 17:
          print("Юность")
        elif age >= 18 and age <= 50:
          print("Взрослый")
        else:
          print("Пожилой")

    except ValueError:
        print("Пожалуйста, введите число")
