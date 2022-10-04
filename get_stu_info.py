import requests
import json


def get_stu_info(sInfo,cookie):
    cookies = {
        'ASP.NET_SessionId': '',
        '__LOGINCOOKIE__': '',
        '__SINDEXCOOKIE__': cookie,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,fr;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'ASP.NET_SessionId=; __LOGINCOOKIE__=; __SINDEXCOOKIE__=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'Origin': 'http://192.168.111.51',
        'Referer': 'http://192.168.111.51/gmis/(S('+sInfo+'))/student/pygl/xskbcx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'kblx': 'xs',
        'termcode': '28',
    }

    response = requests.post('http://192.168.111.51/gmis/(S('+sInfo+'))/student/pygl/py_kbcx_ew',
                             cookies=cookies, headers=headers, data=data, verify=False)
    return response.json()['rows']



