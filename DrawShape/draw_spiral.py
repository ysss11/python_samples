# 渦まきを描画
from turtle import fd, left


def swirl(num):
    for i in range(num):
        fd(50)
        left(10 + i)


swirl(100)
input()  # Enterを押して終了します。
