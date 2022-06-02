# pylint: disable=duplicate-code
from time import sleep
from threading import Thread

target_time = 10


def up_timer(time):
    for i in range(1, time + 1):
        print(i)
        sleep(1)
    print("カウントアップ終了！")


def down_timer(time):
    for i in range(time, 0, -1):
        print(i)
        sleep(1)
    print("カウントダウン終了！")


# Threadインスタンスをタイマーごとに生成する
thread_1 = Thread(target=up_timer, args=(target_time,))
thread_2 = Thread(target=down_timer, args=(target_time,))

# スレッドを起動する
thread_1.start()
thread_2.start()
