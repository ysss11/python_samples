from time import sleep

target_time = 10

def up_timer(time):
    for i in range(1,time+1):
        print(i)
        sleep(1)
    print("時間です！")

def down_timer(time):
    for i in range(time, 0, -1):
        print(i)
        sleep(1)
    print("時間です！")

up_timer(target_time)
down_timer(target_time)
