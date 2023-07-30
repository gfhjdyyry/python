from random import randint

print("Здравствуй, дорогой игрок! Вы будете играть в игру 'Угадай цифру'")
x = randint(1, 100)
game = 1
while game == 1:
    try:
        print("Введите число")
        z = int(input())
        if x == z:
            print("Молодец, вы угадали")
            game = 0
        else:
            if x > z:
                print("Неправильно, больше")
            else:
                print("Неправильно, меньше")
    except ValueError:
        print("Пожалуйста, введите число")

print("Спасибо, что сыграл")