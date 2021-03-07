# slackにPythonからメッセージを送信する方法
import slackweb


def message_to_slack(message):
    slack = slackweb.Slack(url="webhookで取得した値を設定")
    slack.notify(text=message)

message_to_slack("test message")
