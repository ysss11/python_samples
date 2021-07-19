# 絵を描画して表示するプログラム
## プログラム一覧
[四角形を描画](#四角形を描画)  
[五角形を描画](#五角形を描画)  
[渦巻を描画](#渦巻を描画)  
[花を描画](#花を描画)  
[円を描画](#円を描画)  
[星を描画](#星を描画)  
[太陽のような絵を描画](#太陽のような絵を描画)  
[三角形を描画](#三角形を描画)  
[魔法陣のような絵を描画](#魔法陣のような絵を描画)  


### 四角形を描画
#### 内容
```md
draw_rectangle.pyは四角形を描画します。
right(90)で90度方向変換しそれを4回実施して四角形を描画しています。
```
#### 使い方
```python
python draw_rectangle.py
```
#### 出力結果
![rectangle](image/rectangle.JPG)

### 五角形を描画
#### 内容
```md
draw_pentagon.pyは五角形を描画します。
left(72)で72度方向変換しそれを5回実施して五角形を描画しています。
```
#### 使い方
```python
python draw_pentagon.py
```
#### 出力結果
![pentagon](image/pentagon.JPG)

### 渦巻を描画
#### 内容
```md
draw_spiral.pyは渦巻を描画します。
left(10 + i)でiにはrangeで数値を渡すことによりleftの値で動きを変え渦まきを再現している。
```
#### 使い方
```python
python draw_spiral.py
```
#### 出力結果
![spiral](image/spiral.JPG)

### 花を描画
#### 内容
```md
draw_flower.pyは花を描画しています。
円を1回書き再度角度を変えて円を書く。それを10回書くことにより花を描画している。
```
#### 使い方
```python
python draw_flower.py
```
#### 出力結果
![flower](image/flower.JPG)

### 円を描画
#### 内容
```md
draw_circle.pyは円を描画しています。
円を描画するためleft(18)を20回することで、360度(円)を描画しています。
```
#### 使い方
```python
python draw_circle.py

```
#### 出力結果
![circle](image/circle.JPG)

### 星を描画
#### 内容
```md
draw_stars.pyは星を描画しています。
left(144)で5回実施することで一筆で書ける星が書けます。
```
#### 使い方
```python
python draw_stars.py
```
#### 出力結果
![stars](image/stars.JPG)

### 太陽のような絵を描画
#### 内容
```md
draw_sun.pyは太陽のような絵を描画しています。
```
#### 使い方
```python
python draw_sun.py
```
#### 出力結果
![sun](image/sun.JPG)

### 三角形を描画
#### 内容
```md
draw_traiangle.pyは三角形を描画しています。
left(120)に設定して三回実施することで正三角形を描画しています。
```
#### 使い方
```python
python draw_traiangle.py
```
#### 出力結果
![traiangle](image/traiangle.JPG)

### 魔法陣のような絵を描画
#### 内容
```md
draw_magic_circle.pyは魔法陣のような絵を描画しています。
```
#### 使い方
```python
python draw_magic_circle.py
```
#### 出力結果
![magic_circle](image/magic_circle.JPG)
