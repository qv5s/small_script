import json
import urllib.request
url='http://freegeoip.net/json/'
data=urllib.request.urlopen(url)
data=data.read().decode('utf-8')
d=json.loads(data)
print('本机地址所在国:'+d['country_name'])
print('本机ip地址:'+d['ip'])
print('本机城市:'+d['city'])
print('经纬度:(%f,%f)'%(d['latitude'],d['longitude']))
