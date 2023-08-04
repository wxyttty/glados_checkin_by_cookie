# _*_ coding : gbk _*_
# @Time : 2023/7/31 16:34
# @Author : minglu7
# @File : glados_checkin 访问glados网站，自动签到
# @Project : chatgpt

import requests
import json

url = "https://glados.rocks/api/user/checkin"
payload = {
    'token': 'glados.one'
}
headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
  "Content-Type": "application/json;charset=UTF-8",
  "Cookie": "koa:sess=eyJ1c2VySWQiOjE3MDkzMCwiX2V4cGlyZSI6MTcxNjg2MjQxNzg1MiwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=SjVVHihCG-Qu0B6TFv1KllV6G08;"
}

data = json.dumps(payload)

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)