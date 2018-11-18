# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from movieproject.items import MovieprojectItem


class MmSpider(CrawlSpider):
    name = 'mm'
    allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie/']

    # 根据规则提取所有的页码链接
    page_link = LinkExtractor(allow=r'/movie/\?page=\d')
    # follow : 是否跟进
    rules = (
        Rule(page_link, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
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

            yield item
