# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/25 下午3:13'

import requests
import re
from lxml import etree


def get_score(id):
    #豆瓣评分
    if id == 0:
        return {"douban_score":'0',"imdb_score":'0'}
    url_douban_score = "https://api.douban.com/v2/movie/"+str(id)
    url_douban = "https://movie.douban.com/subject/"+str(id)
    web_douban_score = requests.get(url_douban_score)
    html_douban_score =web_douban_score.text

    pattern = re.compile(r'average.*(\d.\d).*num')  # 查找数字
    douban_score = pattern.findall(html_douban_score)[0]

    #IMDB评分
    web_douban = requests.get(url_douban)
    html_douban = web_douban.text
    pattern2 = re.compile(r'(http://www.imdb.com/title/.*\d+)"')
    url_imdb = pattern2.findall(html_douban)
    web_imdb = requests.get(url_imdb[0])
    html_imdb = web_imdb.text

    select = etree.HTML(html_imdb)
    imdb_score = select.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/strong/span/text()')[0]

    score ={"douban_score":douban_score,"imdb_score":imdb_score}
    return score




