## 郵便番号データベースを用いて住所や郵便番号を検索するプログラム
### 内容
```md
郵便番号データベースのデータを用いて住所や郵便番号を検索するプログラム
引数に渡す値を用いて検索する
郵便番号データベースのデータは「KEN_ALL.zip」を解凍して利用してください。
```
以下の検索方法がある
 - 郵便番号から検索する
 - 住所から郵便番号を検索する
 - 郵便番号と住所から検索する

### 引数について
```
D:\JapanPostSearch>python search.py -h
usage: search.py [-h] [--postal_code POSTAL_CODE] [--addresses ADDRESSES]

optional arguments:
  -h, --help            show this help message and exit
  --postal_code POSTAL_CODE
                        郵便番号は xxxxxxx 形式で指定すること
  --addresses ADDRESSES
                        住所を入力して郵便番号を検索する
```

### 使い方
##### プロジェクトの初期化
```
pipenv --python 3.7
```
#### 仮想環境に入る
```
pipenv shell
```
#### 実行と出力結果
郵便番号と住所から検索する場合
```
D:\JapanPostSearch>python search.py --postal_code 1110032 --addresses 浅草
1110032 東京都台東区浅草
1110053 東京都台東区浅草橋
1110035 東京都台東区西浅草
1110025 東京都台東区東浅草
1110041 東京都台東区元浅草
5030947 岐阜県大垣市浅草
```

住所から郵便番号を検索する場合
```D:\JapanPostSearch>python search.py --addresses 浅草
1110032 東京都台東区浅草
1110053 東京都台東区浅草橋
1110035 東京都台東区西浅草
1110025 東京都台東区東浅草
1110041 東京都台東区元浅草
5030947 岐阜県大垣市浅草
```

郵便番号から検索する場合
```
D:\JapanPostSearch>python search.py --postal_code 1510064
1510064 東京都渋谷区上原
```

> 参考  
> https://news.mynavi.jp/article/zeropython-11/  
