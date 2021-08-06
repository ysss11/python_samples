# Speech Recognition　を用いて音声データの文字起こし
import speech_recognition as sr

# 音声ファイルを定義
AUDIO_FILE = 'resources\public_audio_ja-JP_Broadband-sample.wav'
#AUDIO_FILE = "resources\public_audio_ja-JP_Narrowband-sample.wav"

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as s:
    audio = r.record(s)

print('音声データの文字起こし結果：\n', r.recognize_google(audio, language='ja'))
