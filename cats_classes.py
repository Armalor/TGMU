class Animal:

    def __init__(self, name, weight, whool=None, eyes_color=None, dimension=None):
        self.name = name
        self.weight = weight  # Килограммы
        self.whool = whool
        self.eyes_color = eyes_color
        self.dimension = dimension

    def __str__(self):
        ret = f'Объект {self.__class__.__name__}: имя={self.name}; вес={self.weight}кг;'
        if self.whool:
            ret += f' шерсть={self.whool}'
        return ret




if __name__ == '__main__':
    a = Animal('Животне', 5, whool="Длинная, волосатая")

    print(a)
