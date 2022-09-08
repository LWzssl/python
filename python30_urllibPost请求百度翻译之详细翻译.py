# _*_ conding : utf-8 _*_
# @Time : 2022/9/7 18:08
# @Author : LWQaQ
# @File : python30_urllibPost请求百度翻译之详细翻译
# @Project : PycharmProjects
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    "Accept": "*/*",
    # "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Acs-Token": "1662534188435_1662545399082_HzFyFkQ9mSh/JYxzXDsPsdaFYC4Pp0dquTPhLUGL8/64/MuILLzVRdnRxTaS7qtg0eFrwXrrEzJ52gBJnnL48LScFWd2u/3BhoP162CCkWmSjHWBJ+MYUqffiekIb+TiD0brR2NqzYSA5eNSlpCWpx7iIgj8H45aZNm8dz1PG4aBzLniUiMWGSvJhBZMwTSLefXQDMnV0BdfQ5vM9SW0lOm1xc21vZD4bOUgu4hhDsjzNWtgihuOQcyqL94qnl4sj8kCP4xxL3ELbGD+VCGJ+BbF4Wwo/sVhYB7l5vqZyNlCGzSvzfDA+gFrb4QB0rHI",
    "Connection": "keep-alive",
    "Content-Length": "135",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "BIDUPSID=A88BCE84ACCEDC9012B2AF5FA8D86829; PSTM=1623751238; __yjs_duid=1_3dda64aa7f0dcf42c993b3a01e12d5b21623858424347; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; HISTORY_SWITCH=1; BDUSS=dUfjZLWnZHQnZ6bDNieTVodEEzdTI4MWpvdVFFUkN3NXFpNmZSNHh2TWVjRVJpRVFBQUFBJCQAAAAAAAAAAAEAAACWFgxyNzTO0tKysrvP69Xi0fkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB7jHGIe4xxifm; BDUSS_BFESS=dUfjZLWnZHQnZ6bDNieTVodEEzdTI4MWpvdVFFUkN3NXFpNmZSNHh2TWVjRVJpRVFBQUFBJCQAAAAAAAAAAAEAAACWFgxyNzTO0tKysrvP69Xi0fkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB7jHGIe4xxifm; BAIDUID=CF523924711F4FAD8771B66F6D2B6FD6:FG=1; APPGUIDE_10_0_2=1; BAIDUID_BFESS=CF523924711F4FAD8771B66F6D2B6FD6:FG=1; delPer=0; PSINO=2; BA_HECTOR=8525akag05ak2405a0a5jfpq1hhgo8117; ZFY=JqDMmqXFVtIWIdDPmPVyUyfYx:B4geMeLhYQLuyY:Ah5o:C; H_PS_PSSID=26350; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1661073604,1662269646,1662544085; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1662544113; ab_sr=1.0.1_OGY1MzhmZWFmMzhmNWUxYzRkZWE4NWUwM2Q4MTYwZWZjNzA3Zjg3ZDQxY2U2NjkxNTk0MWViYjc3NGY0NzQ1OTRiZjMwOTljZDU2MzVmMmI1MGU0NzhlMmI2N2MyNjY3ZmVkMTQ4MDJlNDRjMThmNjkxMjk3MzdiMmQ3NzdjOTM5ZTllMmQ0Y2I5MmRmZDBmYjk2YmM3N2RkYjcxNjFkMWU1NDczZWIwZDA4YTc3YmExY2ZjMTk2NGQzNDU5MWNi",
    "Host": "fanyi.baidu.com",
    "Origin": "https://fanyi.baidu.com",
    "Referer": "https://fanyi.baidu.com/?aldtype=16047",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

# post请求的参数必须要进行编码
data = {
    "from": "en",
    "to": "zh",
    "query": "coco",
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "905595.602698",
    "token": "fe453c604fc14cfa9bbfc95797d4044c",
    "domain": "common"
}
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象定制
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)
