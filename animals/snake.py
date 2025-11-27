from animal import Animal
from time_logger import time_logger
from random import choice


class Snake(Animal):

    # @time_logger
    def voice(self):
        choices = ['шипит', 'молчит']
        print(f'Змея {self.name} {choice(choices)}')


if __name__ == '__main__':
    s = Snake('Питоняшка', 10)

    s.voice()




