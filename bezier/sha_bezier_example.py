from drawzero import *
from random import uniform


def move(v, w, t):
    return [v[0] * (1 - t) + w[0] * t, v[1] * (1 - t) + w[1] * t]


def add(v, w):
    return [v[0] + w[0], v[1] + w[1]]


def sub(v, w):
    return [v[0] - w[0], v[1] - w[1]]


def gen_pt():
    return [uniform(0, 1000), uniform(0, 1000)]


def gen_continue():
    # Нужно выбрать такие точки a и b, что a, b, b+(b-a) все лежат внутри квадрата
    while True:
        p2 = gen_pt()
        p3 = gen_pt()
        p4 = add(p3, sub(p3, p2))
        if 0 <= p4[0] <= 1000 and 0 <= p4[1] <= 1000:
            return p2, p3, p4


pts = [gen_pt(), gen_pt(), *gen_continue()]

while True:
    for i in range(100):
        t = i / 100
        a, b, c, d, _ = pts
        p, q, r = move(a, b, t), move(b, c, t), move(c, d, t)
        x, y = move(p, q, t), move(q, r, t)
        z = move(x, y, t)
        clear()
        filled_circle('red', z, 10)
        # filled_circle('blue', b, 2)
        # filled_circle('blue', c, 2)
        # filled_circle('yellow', d, 2)
        tick()
    print('next curve')
    # Выбираем новые точки.
    # В качестве первой — последнюю из предыдущей кривой
    # В качестве второй — последнюю + вектор предпосл-посл
    pts = [pts[-2], pts[-1], *gen_continue()]