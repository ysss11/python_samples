## PDFを結合するプログラム

### 内容
```md
PDFファイル2つを結合したり、PDFに挿入したりするプログラム
simple_mergeで単純に結合
insertでPDFに挿入
```

### 事前に必要なもの
dataフォルダ配下にJava.pdf,Python.pdfを置く。ここに操作するPDFファイルを置く。

### 使い方
##### プロジェクトの初期化
```
pipenv --python 3.7
```
#### 仮想環境に入る
```
pipenv shell
```
仮想環境から出る場合はexitなどを入力
#### PDFファイルを編集するためのモジュールをインストール
```
pip install PyPDF2
```

#### ファイルの実行
```
python pdf_marge.py
```
実行結果はdataフォルダに、sample_merge.pdfとsample_insert.pdfとして作成されます。

# 参考
> https://note.nkmk.me/python-pypdf2-pdf-merge-insert-split/  
