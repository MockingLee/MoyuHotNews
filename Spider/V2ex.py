import requests
import json
import pymysql
url = 'https://www.v2ex.com/api/topics/hot.json'
print(url)
response = requests.get(url)

response = json.loads(response.text)

# db = pymysql.connect(host='db.pkmgtdz.top',
#                              port=3306,
#                              user='lee',
#                              password='123',
#                              db='MoyuHotNews',
#                              charset='utf8')
#
# cursor = db.cursor()

print(response)
for i in response:
    print(i['title'])
    print(i['url'])
