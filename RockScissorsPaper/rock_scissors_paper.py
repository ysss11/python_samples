import math
import random

# じゃんけんの手のリスト
hand_list = ["グー", "チョキ", "パー"]
judge_list = ["あいこ", "負け", "勝ち"]
score = 0
count = 0

def judge(x, y):
    """ じゃんけんの判定関数 """
    score = (x - y + 3) % 3
    if score == 0:
        result = judge_list[score]
        _score = 0
    elif score == 1:
        result = judge_list[score]
        _score = 0
    else:
        result = judge_list[score]
        _score = 1
    return result, _score

if __name__ == '__main__':
    while True:
        print()
        print("----------------------------")
        print("じゃんけんスタート")
        print("下記の数値を入力してください。")
        print("0:グー 1:チョキ 2:パー 3:成績を表示 4:じゃんけん終了")
        print("じゃんけんに勝ったら+1点")
        print("----------------------------")
        player = input(">>> ")

        try:
            player = int(player)
            if player > 4:
                raise ValueError
        except ValueError:
            print("0~4の間で値を入力してください。")
            continue

        if player == 3:
            if count > 0:
                print("-----成績表-----")
                win = math.floor(score / count * 100)
                print(f"{count} 戦")
                print(f"スコア：{score} 点")
                print(f"勝率：{win} %")
            else:
                print("まだじゃんけんしていません。")
        elif player == 4:
            break
        else:
            # コンピュータの手をランダムに決定
            com = random.randint(0, 2)

            print(f"あなたは{hand_list[player]}を出しました。")
            print(f"コンピュータは{hand_list[com]}を出しました。")

            # 勝敗判定
            result, _score = judge(player, com)
            count += 1
            score += _score
            print(f"じゃんけんの結果：{result}\n")
