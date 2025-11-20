import random


class NotImplementedException(Exception):
    ...


def roulette():
    while True:

        print("Отлично, делайте ставку!")

        s = input("На какое поле ставить (0-32)?")

        if not s.isdigit():
            print('Нужно ввести число!')
            continue

        s = int(s)

        win = random.randint(0, 32)

        if s == win:
            print("Вы победили, ура! Еще?")
        else:
            print(f"Вы проиграли, выпало {win}, увы!")

        repeat = input('Сыграем еще? (да/нет)')

        if repeat.strip().lower() == 'нет':
            break


def poker():
    raise NotImplementedException("Пока нет других участников, извините!")


def one_armed_bandit():
    raise NotImplementedException("Однорукий бандит Вася пока в отпуске, извините!")


print("Приветствуем вас в нашем казино!")

enter = input("Желаете зайти (да/нет)?")

if 'да' == enter:
    print("Добро пожаловать!")

    choose = input("Во что будете играть: рулетка (1), покер (2), однорукий бандит (3)")

    try:
        if '1' == choose:
            roulette()
        elif '2' == choose:
            poker()
        elif '3' == choose:
            one_armed_bandit()

    except NotImplementedException as err:
        print(f'Не работает: {err}')

    print('Заходите еще!')

elif 'нет' == enter:
    print("Будем ждать!")
