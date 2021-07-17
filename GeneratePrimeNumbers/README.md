## 100までの素数を表示するプログラム
### 内容
```md
generate_prime_numbers.pyはNumPyを利用して素数を見つけるプログラム
is_prime関数で素数の判定を実施し、NumPyのvectorizeで配列の各要素ごとに判定するようにしています。

generate_prime_numbers2.pyはジェネレータを利用して素数を出力しています。

generate_prime_numbers3.pyは対象の値を2からその対象の値の手前まで割っていき、割り切れた場合は素数ではないため、それを判断対象とする。
```
### 使い方
```python
python generate_prime_numbers.py
[ 2  3  5  7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97]
```
```python
python generate_prime_numbers2.py
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```
```python
python generate_prime_numbers3.py
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```
