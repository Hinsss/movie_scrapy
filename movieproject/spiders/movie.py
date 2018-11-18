# -*- coding: utf-8 -*-
import scrapy
from movieproject.items import MovieprojectItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie/']

    url = 'http://www.id97.com/movie/?page={}'
    page = 1

    def parse(self, response):
        # 首先找到所有的div
        div_list = response.xpath('//div[contains(@class,"col-xs-1-5")]')
        # 遍历div，依次获取每一个信息
        for odiv in div_list:
            # 创建一个item
            item = MovieprojectItem()
            item['post'] = odiv.xpath('.//img/@data-original').extract_first()
            item['name'] = odiv.xpath('.//img/@alt').extract_first()
            item['score'] = odiv.xpath('.//h1/em/text()').extract_first().strip(' -')
            # 获取类型
            item['_type'] = odiv.xpath('.//div[@class="otherinfo"]').xpath('string(.)').extract_first()
            # 获取详情页面链接
            detail_url = odiv.xpath('.//h1/a/@href').extract_first()
            # 向详情页发送请求, 并且通过meta将item传递过去
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

        # 获取其它页面的代码自己添加一下

    def parse_detail(self, response):
        # 通过response的meta属性，获取到参数item
        item = response.meta['item']
        item['director'] = response.xpath('//div[@class="col-xs-8"]/table/tbody/tr[1]/td[2]/a/text()').extract_first()
        item['editor'] = response.xpath('//div[@class="col-xs-8"]/table/tbody/tr[2]/td[2]/a/text()').extract_first()
        # '张静初 / 龙品旭 / 黎兆丰 / 王同辉 / 张国强 / 叶婉娴 / 丽娜 / 吴海燕 / 吴若林 / 喻引娣 显示全部'
        item['actor'] = response.xpath('//div[@class="col-xs-8"]/table/tbody/tr[3]/td[2]').xpath('string(.)').extract_first().replace(' ', '').replace('显示全部', '')
        # 片长 
        lala = response.xpath('//div[@class="col-xs-8"]/table/tbody/tr[8]/td[2]/text()').extract_first()
        if lala and ('分钟' in lala):
            item['long_time'] = lala
        else:
            item['long_time'] = ''
        # 电影介绍
        item['introduce'] = response.xpath('//div[@class="col-xs-12 movie-introduce"]').xpath('string(.)').extract_first().replace('\u3000', '').replace('展开全部', '')
        # 电影链接
        # item['download_url'] = response.xpath('')
        yield item


