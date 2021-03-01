"""
素数を生み出すジェネレータを定義するジェネレータ関数
"""

def prime():
    yield 2 # 2を出力して一時停止
    yield 3 # 3を出力して一時停止
    p = 5
    while True:
        for i in range(3, p, 2):
            if p % i == 0:
                break
            if i > p ** 0.5:
                yield p # pを出力して一時停止
                break
        p += 2

g2 = prime()
# 25個の素数を出力(100までの素数の数が25個のため)
for p in range(25):
    print(next(g2), end=" ")
