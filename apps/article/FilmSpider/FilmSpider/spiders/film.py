# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/31 下午5:03'
# -*- coding: utf-8 -*-
import scrapy
import re
import os
import time
import requests
import datetime
from scrapy.http import Request
from urllib import parse


from article.FilmSpider.FilmSpider.utils.common import get_md5
from article.FilmSpider.FilmSpider.items import FilmspiderItem



class FilmSpider(scrapy.Spider):
    name = 'film'
    allowed_domains = ['1905.com']
    start_urls = ['http://www.1905.com/list-p-catid-220.html']

    def parse(self, response):
        #1
        post_nodes = response.xpath("//*[@id='content']/div/div[1]/div/section/ul/li/a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=post_url,meta={"front_image_url": image_url}, callback=self.parsedetail)
        #2
        next = response.xpath('//*[@id="paging"]/a[@class="next"]/@href').extract_first("")
        if next:
            yield Request(url=next,callback=self.parse)

    def parsedetail(self,response):
        #具体字段
        title = response.xpath('//*[@id="contentNews"]/h1/text()').extract_first(" ")
        #创建时间
        create_date= response.xpath('//*[@id="contentNews"]/div[1]/span[1]/text()').extract_first(" ").replace("时间：","")
        #正文
        context = response.xpath('//*[@id="contentNews"]/div[2]/p').extract()
        article = ""
        for phase in context:
            article += phase
        front_image_url = response.meta.get("front_image_url", "")

        film_iteam = FilmspiderItem()
        film_iteam["title"] = title
        film_iteam["create_date"]=create_date
        film_iteam["article"] = article
        film_iteam["front_image_url"]=[front_image_url]
        film_iteam["url"] = response.url
        film_iteam["url_object_id"]=get_md5(response.url)


        pattern = re.compile(r'\d+/\d+/(.*)')
        name = pattern.findall(front_image_url)[0]
        film_iteam["front_image_name"]="article/"+name

        try:
            r = requests.get(front_image_url)
            filename = '../../../../media/article/{}'.format(name)
            with open(filename, 'wb') as fo:
                fo.write(r.content)
        except:
            print('Error')

        yield film_iteam

        pass
