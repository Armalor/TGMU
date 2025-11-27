from animals import Animal, Cat, Dog


if __name__ == '__main__':
    abyss = Cat('Абис', 4, whool='короткая коричневая')
    blueberry = Cat('Черника', 4.5, whool='черная средняя')

    dog1 = Dog('Шашлык', 10, 'черная короткая')

    print(abyss)
    print(blueberry)
    abyss.voice()
    blueberry.voice()

    print(dog1)
    dog1.voice()
