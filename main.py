import requests
import time
import json
from requests.exceptions import RetryError

headers = {
    "Host": "anti-epidemic.ecnu.edu.cn",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "Referer": "https://servicewechat.com/wxfcaebbc17bdc154b/35/page-frame.html",
    "content-type": "application/json",
    "Accept-Encoding": "gzip, deflate, br"}

url = r'https://anti-epidemic.ecnu.edu.cn/clock/mini/wx/new?open_key=6126557d237e6d2a584da65e'

res = requests.get(url,headers=headers)
minitoken = res.json()['message']

headers = {
    "Host": "anti-epidemic.ecnu.edu.cn",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "Referer": "https://servicewechat.com/wxfcaebbc17bdc154b/35/page-frame.html",
    "content-type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "MiniToken": minitoken}

body = {
    "health" : "健康，未超过37.3",
    "location" : "在上海不在校-上海市/上海市/闵行区",
    "number" : "你的学号",
    "reason" : "无",
    "recordTime" : str(round(time.time()) * 1000),
    "token" : "你的token，可以通过fiddler获取"
}
payload = json.dumps(body)
url = r'https://anti-epidemic.ecnu.edu.cn/clock/mini/record'
res = requests.put(url,headers=headers,data=payload)
print(res.text)
