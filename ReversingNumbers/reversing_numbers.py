def reverseNumber(number):
    result = ''
    while number:
        result += str(number % 10)
        number = number // 10
    return result

def reverseNumberForSlice(number):
    return str(number[::-1])

if __name__ == '__main__':
    input_num = input("数値を入力してください。>>> ")
    # 数値チェックをいれる
    if input_num.isdigit():
        number = reverseNumber(int(input_num))
        print(f"reverseNumber result : {number}")

        value = reverseNumberForSlice(str(input_num))
        print(f"reverseNumberForSlice result : {value}")
    else:
        print("数値を入力してください。")
