import sys


def add(a, b):
    ans = a
    for _ in range(1, b + 1):
        ans += 1
    return ans


def sub(a, b):
    ans = a
    for _ in range(1, b + 1):
        ans -= 1
    return ans


def multi(a, b):
    ans = 0
    for _ in range(1, b + 1):
        ans = add(ans, a)
    return ans


def div(a, b):
    ans = 0
    while(a >= b):
        a = sub(a, b)
        ans += 1
    return ans


if __name__ == '__main__':
    args = sys.argv
    ans = 0
    if 2 <= len(args):
        if args[1] == "+":
            ans = add(int(args[2]), int(args[3]))
            print("operator:", args[1])
        elif args[1] == "-":
            ans = sub(int(args[2]), int(args[3]))
            print("operator:", args[1])
        elif args[1] == "*":
            ans = multi(int(args[2]), int(args[3]))
            print("operator:", args[1])
        elif args[1] == "/":
            ans = div(int(args[2]), int(args[3]))
            print("operator:", args[1])
        else:
            print("演算子(+,-,*,/)を入力してください。")

        print("answer:", ans)
    else:
        print('引数が未入力です。')
