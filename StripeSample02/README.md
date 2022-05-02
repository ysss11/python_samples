# Web サイトまたはアプリケーションにカスタムの Stripe 支払いフォームを埋め込む方法

## プロジェクトの初期化
pipenv --python 3.7

## 仮想環境に入る
pipenv shell

## インストール

```
pip install -r requirements.txt
```

## サーバの起動

```
set FLASK_APP=server.py
python -m flask run --port=4242
```

## client アプリのビルド


```
npm install
```

## client アプリの起動
```
npm start
```


## アクセス

[http://localhost:3000/checkout](http://localhost:3000/checkout)


## 参考

> https://stripe.com/docs/payments/quickstart
