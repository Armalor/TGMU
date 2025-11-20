
def circle_square(radius):
    sq = radius * radius * 3.1415926535
    return sq


def rectangle_square(a, b):
    return a * b


def fac1(n):
    ret = 1
    while n > 1:
        ret *= n
        n -= 1

    return ret


def fac_r(n):
    if n < 2:
        return 1

    return n * fac_r(n-1)


s1 = 10 * 10 * 3.1415926
print(f'Площадь круга радиусом 10 равна {s1}')

s2 = circle_square(radius=15)
print(f'Площадь круга радиусом 15 равна {s2}')

s3 = circle_square(radius=23)
print(f'Площадь круга радиусом 23 равна {s3}')


r1 = rectangle_square(10, 12)
print(f'Площадь прямоугольника со сторонами 10, 12 равна {r1}')

r2 = rectangle_square(a=100, b=122)
print(f'Площадь прямоугольника со сторонами 100, 122 равна {r2}')


n = 0
f1 = fac1(n)
print(f'Факториал числа {n} равен {f1}')

n = 1
f1 = fac_r(n)
print(f'Факториал числа {n} равен {f1}')

n = 3
f1 = fac_r(n)
print(f'Факториал числа {n} равен {f1}')

n = 5
f1 = fac_r(n)
print(f'Факториал числа {n} равен {f1}')

n = 6
f1 = fac_r(n)
print(f'Факториал числа {n} равен {f1}')
