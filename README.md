# set_time

Pythonを使わないで時刻合わせ
```
sudo date -s "$( wget -q http://worldtimeapi.org/api/timezone/Asia/Tokyo -O - | grep -oE \"datetime\":\"[^\"]* | sed s/\"datetime\":\"// )"
```
