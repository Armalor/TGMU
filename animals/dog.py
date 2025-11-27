from .animal import Animal
from random import choice


class Dog(Animal):
    def voice(self):
        choices = ['лает', 'громко лает', 'храпит как свинья']
        print(f'Кот {self.name} {choice(choices)}')