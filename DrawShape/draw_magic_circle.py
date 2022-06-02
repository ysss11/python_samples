# 魔法陣を描画

from turtle import fd, left


def triangle():
    for _ in range(3):
        fd(250)
        left(120)


for _ in range(10):
    triangle()
    left(36)
input()
