import re
import requests
import json


def gethtml():
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        coo = 'tt_webid=6796837484019926535; s_v_web_id=verify_k6zutinu_rjv8g5On_gIuC_45pV_8dnF_Z9xtAWBWsB9a; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=uq33rx4i71582512058231; csrftoken=47b19ac2812754ff996f3003fee6e991; tt_webid=6796837484019926535; ttcid=9202e774c50c4b98b98ae73e7248d46537; sso_uid_tt=76aae7b4af89e3595fcf40e618897a12; sso_uid_tt_ss=76aae7b4af89e3595fcf40e618897a12; toutiao_sso_user=487d7486cd86fa94c5897f4ad1de8683; toutiao_sso_user_ss=487d7486cd86fa94c5897f4ad1de8683; sid_guard=1a14e0a542a71ec97ea3c9001e5075ff%7C1582512083%7C5184000%7CFri%2C+24-Apr-2020+02%3A41%3A23+GMT; uid_tt=7f1a8da15d27916c0b33d30e0912bdb5; uid_tt_ss=7f1a8da15d27916c0b33d30e0912bdb5; sid_tt=1a14e0a542a71ec97ea3c9001e5075ff; sessionid=1a14e0a542a71ec97ea3c9001e5075ff; sessionid_ss=1a14e0a542a71ec97ea3c9001e5075ff; tt_scid=lkT4VX1nmFCOtTOlZ9NMQj91S-lEDkhle9g2UgL1gRDr5nPLeWILw8IrEjDh5anr7a9b'
        cookies = {}
        for line in coo.split(';'):
            name, value = line.strip().split('=', 1)  # strip()同时去掉开头和末尾的空格
            cookies[name] = value
        r = requests.get("https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1"
                         "&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A175FE5523C37E5&cp"
                         "=5E537387BEB50E1&_signature"
                         "=rPDweAAgEBBqp0n1CaoUDqzwsWAAPKyZrl5SGgrzlI5og5HBzwlDLDtTcHyqlKG6x1Sou"
                         ".BwPKYu2rfd9t4xgJu6gl6SsEnUpb1JmcIsRYUvTlMQdqPlN8VN76TA..z4g7U", cookies=cookies,
                         headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("出现异常:%s" % e)


if __name__ == '__main__':
    wbhtml = gethtml()
    html = json.loads(wbhtml)
    print("热点新闻:")
    html = str(html)    # 必须进行转换，否则会报错,转换过后为一字典
    news = re.findall(r"\'title\': \'.*?\'",html)
    for i in range(len(news)):
        name = eval(news[i].split(":")[1])
        print(name)
