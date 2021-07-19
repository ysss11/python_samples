# 九九を表形式で出力
if __name__ == '__main__':
    kuku = [(x, y, x * y) for x in range(1, 10) for y in range(1, 10)]
    table = ''
    # x:xの段
    for x, y, z in kuku:
        table += '{0:5d}'.format(z)
        if y == 9:
            table += '\n'
    print(table)
