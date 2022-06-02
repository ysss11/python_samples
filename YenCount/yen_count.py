YEN_TYPES = [10000, 5000, 1000, 500, 100, 50, 10, 1]


def getYenCount(money):
    count = [0] * len(YEN_TYPES)
    for i in range(0, len(YEN_TYPES)):
        while money >= YEN_TYPES[i]:
            money -= YEN_TYPES[i]
            count[i] += 1
    return count


if __name__ == '__main__':
    money = input("金額を入力してください。>>> ")
    try:
        money = int(money)
    except ValueError:
        print("数値を入力してください。")

    count = getYenCount(money)
    for i in range(0, len(YEN_TYPES)):
        print(str(YEN_TYPES[i]) + "円\t" + str(count[i]) + "枚")
