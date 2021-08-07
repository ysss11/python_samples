# 英和辞書から word が含まれている語句を抽出する

def search(word):
    with open(".\data\ejdict-hand-utf8.txt", "r", encoding="utf-8") as fp:
        for line in fp:
            # 単語が含まれていたら
            if word in line:
                print(line, end='')

if __name__ == '__main__':
    # 英和辞書のデータを一行ずつ読む
    word = "ball" # 検索単語を指定
    search(word)
