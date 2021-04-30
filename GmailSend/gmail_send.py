from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from os.path import basename

# メール設定の情報
smtp_host = 'smtp.gmail.com'
smtp_port = 587

to_email = '▲▲▲▲▲@gmail.com' # 送りたいアドレス

gmail_account = '▲▲▲▲▲@gmail.com' # Gmailのアドレス
gmail_password = '▲▲▲▲▲' # Gmailのパスワード


def gmail_send():
    # メールの本文
    message = 'メールの本文内容'
    # メールの内容を作成
    msg = MIMEMultipart()
    # 件名
    msg['Subject'] = '件名内容'
    # メール送信元 
    msg['From'] = gmail_account 
    #メール送信先
    msg['To'] = to_email 

    # ファイルを添付
    msg.attach(MIMEText(message))
    # ファイルを添付
    path = "./test.txt"
    with open(path, "rb") as f:
        part = MIMEApplication(
            f.read(),
            Name=basename(path)
        )
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(path)
    msg.attach(part)

    # メールサーバーへアクセス
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_account, gmail_password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    gmail_send()
