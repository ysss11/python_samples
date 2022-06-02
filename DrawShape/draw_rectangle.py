# 四角形を書く
from turtle import fd, right


def square():
    for _ in range(4):
        fd(200)
        right(90)


square()
input()  # Enterを押して終了します。
