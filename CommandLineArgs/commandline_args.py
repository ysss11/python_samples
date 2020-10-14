# coding: UTF-8
"""
引数に指定した件数分の文字列を表示し、指定しない場合は「引数が未入力です。」と表示する
指定する引数は文字列。
例：
python commandline_args.py Python Ruby Java
「Python」が入力されました。
「Ruby」が入力されました。
「Java」が入力されました。
"""
import sys


if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        for i in range(1,len(args)):
            print(args[i])
    else:
        print('引数が未入力です。')
