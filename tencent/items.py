# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 职位名称
    url = scrapy.Field()
    category = scrapy.Field()  # 职位类别
    number = scrapy.Field()  # 招聘人数
    address = scrapy.Field()  # 招聘地点
    pub_time = scrapy.Field()  # 发布时间
    content = scrapy.Field()

    pass
