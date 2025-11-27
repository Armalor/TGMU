from animal import Animal
from random import choice
from time_logger import time_logger


class Dog(Animal):
    @time_logger
    def voice(self):
        choices = ['лает', 'громко лает', 'храпит как свинья']
        print(f'Кот {self.name} {choice(choices)}')


if __name__ == '__main__':
    s = Dog('Котлетос', 10)

    print(s)
    s.voice()
