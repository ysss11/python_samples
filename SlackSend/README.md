## PythonからSlackにメッセージを送信するプログラム
### 内容
```md
pip install slackweb
でSlackへ送信するライブラリを取得します。
slack = slackweb.Slack(url="webhookで取得した値を設定")
上記でオブジェクトを作成し
slack.notify(text=message)
でwebhookで取得した先に送信します。
messageに出力するメッセージを記載します。
```
### 使い方
```md
pip install slackweb

python slack_python.py
```
### 出力結果
Slackの出力結果  
![slack_message](SlackSend/image/slack_message.png)
> 参考  
> https://qiita.com/tmiyama/items/4d1af727829c0fcd301e  
> https://jamstec-iprc.slack.com/?redir=%2Fapps%2Fnew%2FA0F7XDUAZ--incoming-webhook-  
> https://github.com/satoshi03/slack-python-webhook  
