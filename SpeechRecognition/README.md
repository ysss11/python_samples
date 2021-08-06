## 音声データの文字起こしをするプログラム
### 内容
```md
Speech Recognitionをインストールします。
pip install SpeechRecognition
※今回はrequirements.txt ファイルを用意してそちらをインストールするようにします。

SpeechRecognitionで音声データを文字起こしします。
```
### 使い方
```md
pip install -r requirements.txt

python voice_data_transcription.py
```
### 出力結果
public_audio_ja-JP_Narrowband-sample.wav を指定した場合
```
音声データの文字起こし結果：
ご住所の変更でございますね ご連絡ありがとうございます 恐れ入りますが ご契約内容を確認致しますのでお電話をいただいている方は 契約者ご本人様でいらっしゃいますか はい そうです 本人です それではお電話をいただいております お客様のお名前をお願い致します 山田太郎 山田太郎様でいらっしゃいますね では契約者ご本人様確認のため 恐れ入りますが 山田様の生年月日をお願いいたします はい 生年月日が1937年6月17日です
```
public_audio_ja-JP_Broadband-sample.wav を指定した場合
```
音声データの文字起こし結果：
音声認識の現状について教えていただけないでしょうか はい 最近では 音声認識でもディープラーニングがよく使われてますね それはどういったものなのでしょうか 簡単に言えば 脳の仕組みをモデルにした技術です それは難しそうですね 一部では人間の能力を超えるまでになっています
```
> 参考  
> https://su-gi-rx.com/archives/4701  
