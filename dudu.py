# -*- coding=utf-8 -*-
import os
import requests
# import parsel
from parsel import Selector


'''图片保存文件夹'''

dir_name = 'images'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    os.chdir(dir_name)
else:
    os.chdir(dir_name)


def download_one_page_urls(page_url):
    '''拿到网页数据'''
    response = requests.get(page_url)
    print(response.text)
    html = response.text
    # 解析网页数据
    # 把自字符串内容转化成对象
    sel = Selector(html)
    # 提取对象内容
    divs = sel.css('.tagbqppdiv')
    urls = []
    for div in divs:
        # 把对象转化成字符串
        img_url = div.css('img.ui::attr(data-original)').extract_first()
        title = div.css('img.ui::attr(title)').extract_first()
        # print(img_url,title)
        urls.append((img_url, title))
        # print(urls)
    return urls

def download_img(url):
    try:
        # 获取文件内容
        response = requests.get(url[0])
        # 对文件命名
        # 图片是二进制的
        # 文件后缀
        suffix = url[0].split('.')[-1]
        with open(url[1] + '.' + suffix, mode='wb') as f:
            f.write(response.content)
    except Exception as e:
        print('文件名不规范', e)

def download_page_img(page_url):

    urls = download_one_page_urls(page_url)
    for url in urls:
        download_img(url)


if __name__ == '__main__':
    for i in range(1, 10):
        page_url = 'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html'.format(page=i)
        print(page_url)
        # 传入一页就获取一页的所有图片地址
        download_page_img(page_url)
