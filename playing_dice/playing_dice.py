from random import randint

print("""Здравствуй, дорогой игрок!
Вы будете играть в игру 'Игральный кубик'
""")

while True:
    print("Вам выпало число:", randint(1, 6))
    print("Нажмите клавишу 'Enter', чтобы заново бросить кубик")
    z = input()
    if z == "exit":
        print("Выход из программы...")
        break
