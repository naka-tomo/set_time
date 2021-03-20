# set_time

Proxy環境下のUbuntuで時刻合わせ
```
sudo date -s "$( wget -q http://worldtimeapi.org/api/timezone/Asia/Tokyo -O - | grep -oE \"datetime\":\"[^\"]* | sed s/\"datetime\":\"// )"
```
