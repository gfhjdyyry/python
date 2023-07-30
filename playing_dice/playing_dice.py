from random import randint

print("Здравствуй, дорогой игрок!Вы будете играть в игру'Игральный кубик'")

while True:
    x = randint(1, 6)
    print("вам выпало число:", x)
    print("Нажмите клавишу 'Enter' чтобы заново бросить кубик")
    z = input()
    if z == "exit":
        print("Выход из программы...")
        break
