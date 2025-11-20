import random

print("Приветствуем вас в нашем казино!")

enter = input("Желаете зайти (да/нет)?")

# print('да' == enter)

if 'да' == enter:
    print("Добро пожаловать!")

    choose = input("Во что будете играть: рулетка (1), покер (2), однорукий бандит (3)")

    if '1' == choose:

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

    elif '2' == choose:
        print("Пока нет других участников, извините!")
    elif '3' == choose:
        print("Однорукий бандит Вася пока в отпуске, извините!")

    print('Заходите еще!')

elif 'нет' == enter:
    print("Будем ждать!")
