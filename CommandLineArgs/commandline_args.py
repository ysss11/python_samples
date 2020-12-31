# coding: UTF-8
import sys

if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        for i in range(1,len(args)):
            print(args[i])
    else:
        print('引数が未入力です。')
