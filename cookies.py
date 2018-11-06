#coding:gbk
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    # "origin": "https://passport.mafengwo.cn",
    "Referer": "https://passport.mafengwo.cn/",
    'User-Agent': userAgent,
}
header = {
    # "origin": "https://passport.mafengwo.cn",
    "Referer": "https://passport.mafengwo.cn/",
    'User-Agent': userAgent,
}
def mafengwoLogin(account, password):
    # 马蜂窝模仿 登录
    print ("开始模拟登录马蜂窝")

    postUrl = "https://passport.mafengwo.cn/login/"
    postData = {
        "passport": account,
        "password": password,
    }
    responseRes = requests.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    soup = BeautifulSoup(responseRes.text,'html.parser')
    content = soup.select('a')
    print(content)
    for c in content:
	    with open('document.txt','a') as f:
		    f.write('{}\n'.format(c.get_text()))
    #print(f"text = {responseRes.text}")

if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    mafengwoLogin("17340658023", "mafeng@1661")