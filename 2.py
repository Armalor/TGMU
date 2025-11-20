
attempt = 1
while True:
    repeat = input('Крутим дальше?')

    if repeat == 'нет':
        break

    print('Поехали! Попытка', attempt)
    attempt += 1

