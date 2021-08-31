import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.calendar(2021, m=4))

print("--------------------------------")
# 日本語レイアウトはずれてしまう
ltc_ja = calendar.LocaleTextCalendar(locale='ja_jp')
print(ltc_ja.formatmonth(2020, 1))

# HTMLファイルを出力
# 下記はレイアウトが汚いため、きれいにする必要がある。
lc = calendar.HTMLCalendar(calendar.SUNDAY)
body = lc.formatmonth(2021, 1)

f = open("calendar202101.html", "wt")

f.write("<body>" + body + "</body>")
