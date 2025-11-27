from .animal import Animal
from random import choice


class Cat(Animal):
    def voice(self):
        choices = ['мяучет', 'мурчит']
        print(f'Кот {self.name} {choice(choices)}')