# -*- coding=utf-8 -*-
from parsel import Selector
import urllib
import time
import sys
import io
import json
#改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
url = 'http://www.lofter.com/tag/%E5%90%8C%E4%BA%BA?from=tagsearch'
tm = 'number:'+str((int(round(time.time() * 1000))))

data = {
    "callCount=1"
    "scriptSessionId=${scriptSessionId}187"
    
    "c0-param5": "number:0",
    "c0-param6": "number:100",
    "c0-param7": "number:200",
    "c0-param8":  tm,
    "batchId": round(700000) + 100000
}
params = urllib.parse.quote_plus(json.dumps(data)).encode(encoding='utf-8')
req = urllib.request.Request(url, data=params,  method='POST')
response = urllib.request.urlopen(req).read()
txt = str(response, "utf-8")
# print(txt)
print('===========================')
sel = Selector(txt)
divs = sel.css('.w-img')
print(divs[0].css('img').attrib.get("src"))
# print('===========================')
urls = []
for div in divs:
    str = div.css('img').attrib.get("src")
    urls.append(str)
    print(str)

