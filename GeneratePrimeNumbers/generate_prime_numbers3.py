# 素数を生成するプログラム

def prime(val):
    for i in range(2, val + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            print(i)


val = 100  # valまでの数で素数を求める。
prime(val)
