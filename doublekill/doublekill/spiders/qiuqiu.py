# -*- coding: utf-8 -*-
import scrapy
# 导入指定的数据结构
from doublekill.items import DoublekillItem

class QiuqiuSpider(scrapy.Spider):
    name = 'qiuqiu'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    # 爬取多页
    url = 'https://www.qiushibaike.com/8hr/page/{}/'
    page = 1

    def parse(self, response):
        # 首先查找所有的div
        div_list = response.xpath('//div[@id="content-left"]/div')
        # 遍历这个div
        for odiv in div_list:
        	# 创建对象
        	item = DoublekillItem()
        	# 用户头像
        	face = odiv.xpath('.//div[@class="author clearfix"]//img/@src').extract_first()
        	face = 'https:' + face
        	# 用户名
        	name = odiv.xpath('.//div[@class="author clearfix"]//h2/text()').extract_first()
        	name = name.strip('\n')
        	# 用户年龄
        	age = odiv.xpath('.//div[@class="author clearfix"]//div/text()').extract_first()
        	# 内容
        	content = odiv.xpath('.//div[@class="content"]/span/text()').extract_first()
        	content = content.strip('\n')
        	# 好笑个数
        	haha_count = odiv.xpath('./div[@class="stats"]/span[1]//i/text()').extract_first()
        	# 评论个数
        	ping_count = odiv.xpath('./div[@class="stats"]/span[2]//i/text()').extract_first()

        	# 将获取的属性存放到对象中
        	item['face'] = face
        	item['name'] = name
        	item['age'] = age
        	item['content'] = content
        	item['haha_count'] = haha_count
        	item['ping_count'] = ping_count

        	yield item

        # 接着发送请求，爬取下一页
        if self.page <= 5:
        	self.page += 1
        	url = self.url.format(self.page)
        	# 向拼接成功的url发送请求
        	yield scrapy.Request(url, callback=self.parse)

        	# 不能这么做，应该用我们的数据结构
        	# item = {
        	# 	'face': face,
        	# 	'name': name,
        	# 	'age': age,
        	# 	'content': content,
        	# 	'haha_count': haha_count,
        	# 	'ping_count': ping_count
        	# }
        	# print('*' * 50)
        	# print(item)
        	# print('*' * 50)
