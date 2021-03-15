import urllib.request
import json
import os

url = 'http://worldtimeapi.org/api/timezone/Asia/Tokyo'

req = urllib.request.Request(url)
text = urllib.request.urlopen(req).read().decode()

print( json.loads(text)["datetime"]  )
