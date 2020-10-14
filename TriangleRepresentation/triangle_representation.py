# coding: UTF-8
"""
縦10×横10の逆三角形、三角形を表示するプログラム
"""
for i in reversed(range(11)):
    for _ in range(i+1):
        print('●', end='')
    print('\n') 


for i in range(11):
    for _ in range(i+1):
        print('●', end='')
    print('\n')
