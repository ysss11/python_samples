"""
生年月日を使用した年齢の簡易計算プログラム
"""

from datetime import datetime


def CalcAge(birthday):
    if not (birthday.isdigit() and len(birthday) == 8):
        print(f"生年月日を入力してください。 入力値：{birthday}")
        return False
    today = datetime.now().strftime("%Y%m%d")
    return (int(today) - int(birthday)) // 10000


birthday = input("あなたの生年月日を入力してください(yyyyMMdd)＞")
result = CalcAge(birthday)
if result:
    print(f"あなたの年齢は{result}歳です。")
