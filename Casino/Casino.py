from random import randint

print("""Здравствуй, дорогой игрок!
Вы будете играть в игру 'Казино'.
Чтобы выйти из игры введите 'exit'.
""")


while True:
    try:
         z = str(input("Загадайте число, и программа бросит кубик: "))
         if z == "exit":
             print("Выход из программы...")
             break
         x = randint(1, 6)
         if x == int(z):
            print("Правильно")
            print("Если хотите сыграть снова, введите 'Да':")
            i = input()
            if i == "Да":
                continue
            else:
                print("Выход из программы...")
                break
         else:
              print("неправильно, выпало число", x)
    except ValueError:
         print("Введите число")
