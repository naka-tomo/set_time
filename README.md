# set_time

Proxy環境下のUbuntuで時刻合わせ

```
sudo date -s "$(wget -q https://github.com/naka-tomo/set_time/raw/main/set_datetime.py -O - | python)"
```
