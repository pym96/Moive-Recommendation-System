# -*- codeing = utf-8 -*-
# @File: run.py

# - movie_comment.py：电影评论
# - movie_meta.py：电影详情信息
# - movie_subject: 电影的douban_id爬取；

from scrapy.cmdline import execute
# 电影的douban_id爬取
# execute(['scrapy', 'crawl', 'movie_subject'])
# 电影详情信息
# execute(['scrapy', 'crawl', 'movie_meta'])
# 电影评论
execute(['scrapy', 'crawl', 'movie_comment'])

