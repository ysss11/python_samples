# coding: UTF-8
if __name__ == '__main__':
    for i in reversed(range(11)):
        for _ in range(i+1):
            print('●', end='')
        print('')
    print('')
    for i in range(11):
        for _ in range(i+1):
            print('●', end='')
        print('')
