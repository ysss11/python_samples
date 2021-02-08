import random

if __name__ == '__main__':
    num = random.randint(0,10)
    print(num)
    if num == 10:
        print("【大吉】です。")
    elif 6 <= num:
        print("【中吉】です。")
    elif 3 <= num:
        print("【吉】です。")
    elif 1 <= num:
        print("【凶】です。")
    else:
        print("【大凶】です。")
