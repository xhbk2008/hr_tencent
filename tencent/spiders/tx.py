# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TxSpider(scrapy.Spider):
    name = 'tx'
    allowed_domains = ['http://hr.tencent.com/']
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        print(response.url, '8'*88)
        # html = response.body
        item = TencentItem()
        host_url = 'http://hr.tencent.com/'
        # 获取所有职位节点
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # 遍历节点列表 抽取数据
        for node in node_list:
            item['name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['url'] = host_url + node.xpath('./td[1]/a/@href').extract_first()
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract_first()
            item['address'] = node.xpath('./td[4]/text()').extract_first()
            item['pub_time'] = node.xpath('./td[5]/text()').extract_first()
            print(item['name'], item['url'], item['category'], item['number'], item['address'], item['pub_time'])
            # yield scrapy.Request(url=item['url'], callback=self.parse2, meta={'res': item})
            yield item
        next_url = host_url + response.xpath('//*[@id="next"]/@href').extract_first()
        print(next_url, '$'*88)
        yield scrapy.Request(url=next_url, callback=self.parse)


    # def parse2(self, response):
    #     item = response.meta['res']
    #     item['centent'] = response.xpath('//tbody/tr[3]/td/ul/li/text()')
    #     print('1'*50, item, '2'*50)

