# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
	# 爬虫的名字
    name = 'qiubai'
    # 允许的域名, 是一个列表，里面可以放多个，一般都做限制
    allowed_domains = ['www.qiushibaike.com', 'www.baidu.com']
    # 起始url，是一个列表
    start_urls = ['https://www.qiushibaike.com/']

    # 解析函数，重写这个方法，发送请求之后，响应来了就会调用这个方法，函数有一个参数response就是响应内容，该函数对返回值有一个要求，必须返回可迭代对象
    def parse(self, response):
        print('嘿嘿嘿')
        # print(response.text)
        # print(response.body)
        # print('啦啦啦')
        # 首先获取所有的div
        div_list = response.xpath('//div[@id="content-left"]/div')
        # print(div_list)
        # print(len(div_list))
        # print('啦啦啦')
        items = []
        for odiv in div_list:
        	# 获取头像链接
        	face = odiv.xpath('.//div[@class="author clearfix"]//img/@src').extract()[0]
        	# 获取用户名
        	name = odiv.xpath('.//div[@class="author clearfix"]//h2/text()')[0].extract()
        	# 存放到字典中
        	item = {
        		'头像': face,
        		'用户名': name
        	}
        	items.append(item)
        return items
