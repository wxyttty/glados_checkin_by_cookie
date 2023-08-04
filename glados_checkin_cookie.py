# _*_ coding : gbk _*_
# @Time : 2023/7/31 16:34
# @Author : minglu7
# @File : glados_checkin 访问glados网站，自动签到
# @Project : chatgpt

import requests
import json
import os
COOKIE = os.environ.get('COOKIE')
url = "https://glados.rocks/api/user/checkin"
payload = {
    'token': 'glados.one'
}
headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
  "Content-Type": "application/json;charset=UTF-8",
  "Cookie": COOKIE
}

data = json.dumps(payload)

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
