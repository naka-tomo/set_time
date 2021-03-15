# set_time

Proxy環境下のUbuntuで時刻合わせ

```
sudo date -s "$(wget -q https://github.com/naka-tomo/set_time/raw/main/set_datetime.py -O - | python)"
```

Pythonを使わないで時刻合わせ
```
sudo date -s "$( wget -q http://worldtimeapi.org/api/timezone/Asia/Tokyo -O - | grep -oE \"datetime\":\"[^\"]* | sed s/\"datetime\":\"// )"
```
