#!/usr/bin/env python3

import bs4
import requests
import random

if __name__ == '__main__':
    # 获取绝对路径
    url = 'https://www.zhipin.com/boss/update/customgreeting.json'
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'lastCity=101210100; __c=1554616057; JSESSIONID=""; sid=mail_resume_niu; __g=mail_resume_niu; __l=r=https%3A%2F%2Fwww.zhipin.com%2F&l=%2Fsignup.zhipin.com%2F%3Fka%3Dheader-register&g=%2Fm.zhipin.com%2Fresume%2Fpreview4mail%2F4e0125b84e8428b11nd939q6FFFW34m5WPmWQuOlgvLZMhdn2KJX%3Fsid%3Dmail_resume_niu; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1562502292,1563365325; toUrl=/; t=wP8wnvgohhfkFsTs; wt=wP8wnvgohhfkFsTs; _bl_uid=37jzjyqbk7ywsg6wm6q6dpye7wUU; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1564377837; __a=87424242.1554616036.1554616036.1554616057.209.2.208.198',
        'origin': 'https://www.zhipin.com',
        'token': 'RGj4CJ7p6qIRXW8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    param = {
        'content':'我们渴望一位并肩奋斗的小伙伴，有兴趣聊一聊吗？（仅限杭州）-- rufeng',
        'token': 'RGj4CJ7p6qIRXW8',
        'templateId': 'f97af3d607584b413w~~'
    }
    result = requests.post(url, headers=headers, data=param)
    print(result)