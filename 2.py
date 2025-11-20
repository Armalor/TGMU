

repeat = input('Крутим дальше?')

attempt = 1
while repeat.lower() != 'нет':
    print('Поехали! Попытка', attempt)
    attempt += 1
    repeat = input('Крутим дальше?')