# -*- coding=utf-8 -*-
import requests
import unicodecsv as csv
import codecs
import json
from qiniu import Auth, put_file, etag
import qiniu.config
from time import sleep


header = {
'authority': 'bcy.net',
'method': 'GET',
'path': '/apiv3/common/getFeeds?refer=feed&direction=loadmore',
'scheme': 'https',
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cookie': 'tt_webid=6747913873653614094; s_v_web_id=a0eb3512e03c1857c1e357cbaeb43a87; _ga=GA1.2.1601760765.1571121144; PHPSESSID=7903748b0199363199e852efd1d2a1c3; lang_set=zh; mobile_set=no; _gid=GA1.2.1426264270.1571648296; Hm_lvt_330d168f9714e3aa16c5661e62c00232=1571121143,1571125386,1571406957,1571661270; _csrf_token=cbb9529889303076c32cc5679add0808; Hm_lpvt_330d168f9714e3aa16c5661e62c00232=1571666004; _gat_gtag_UA_121535331_1=1',
'referer': 'https://bcy.net/',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
'x-requested-with': 'xmlhttprequest'
}


# connect qiniu
access_key = 'bMsxBlEhchY7vyVNBn8aZRMbQWNIITXd2oewsiQA'
secret_key = 'B2hDo4x-wTlXcKfOUI9wnA3wrn9iGkqHtTV3eoQY'
q = Auth(access_key, secret_key)
bucket_name = 'hualu'
qiniuurl = 'https://image.hualu.yetter.cn/'

# scrap
# url='https://api.bilibili.com/x/v2/reply?type=1&oid=36955225&pn=1'
url = 'https://bcy.net/apiv3/common/getFeeds?refer=feed&direction=loadmore'
response = requests.get(url, headers=header)
result = json.loads(response.text)
i = 0
j = 10000

csvfile = open('scraps.csv', 'wb')
writer = csv.writer(csvfile)

while (j > 0):
    row = result.get('data').get('item_info')
    uname = row[i].get('item_detail').get('uname')
    avatarurl = row[i].get('item_detail').get('avatar').replace('amiddle', 'abig')


    try:
        # download avatar
        avatar = requests.get(avatarurl)
        local_file = 'avatars/' + uname + '.jpg'
        with open(local_file, 'wb') as f:
            f.write(avatar.content)
        # write user nickname
        print(uname)
        # upload avatar
        key = 'app/tavtar/' + str(hash(uname)) + '.jpg'
        token = q.upload_token(bucket_name, key, 3600)
        ret, info = put_file(token, key, local_file)
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(local_file)
        avatarCdnUrl = qiniuurl + key
        # open csv
        writer.writerow([uname, avatarCdnUrl])
    except Exception as e:
        # print('==========================================')
        print('文件名不规范', e)
        # print('==========================================')
    if i < len(row) - 1:
        i = i + 1
    else:
        response = requests.get(url, headers=header)
        result = json.loads(response.text)
        i = 0
        j = j - 1
        # sleep(1000)
        print('-----------------------------')
        print(j)

csvfile.close()
