# Stripe Checkoutのサンプル

## プロジェクトの初期化
pipenv --python 3.11.4

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
npm install -g npm@latest
npm update --include=dev
```

## client アプリの起動
```
npm start
```


## アクセス

[http://localhost:3000/checkout](http://localhost:3000/checkout)


## 参考

> https://stripe.com/docs/checkout/quickstart
> https://qiita.com/HyunwookPark/items/242a8ceea656416b6da8
