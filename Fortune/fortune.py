import random


def fortune(value):

    if value == 10:
        return "【大吉】です。"
    elif 6 <= value:
        return "【中吉】です。"
    elif 3 <= value:
        return "【吉】です。"
    elif 1 <= value:
        return "【凶】です。"
    else:
        return "【大凶】です。"


if __name__ == '__main__':
    num = random.randint(0, 10)
    print(num)
    print(fortune(num))
