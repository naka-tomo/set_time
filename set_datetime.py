import urllib.request
import json
import os

url = 'http://worldtimeapi.org/api/timezone/Asia/Tokyo'

req = urllib.request.Request(url)
text = urllib.request.urlopen(req).read().decode()
print(text)

print( json.loads(text) )
os.system( "sudo date -s " + json.loads(text)["datetime"]  )