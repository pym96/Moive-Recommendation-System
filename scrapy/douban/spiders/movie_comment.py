import random
import string
import time
from lxml import etree
from scrapy import Request, Spider

import douban.database as db
from douban.items import Comment

cursor = db.connection.cursor()


class MovieCommentSpider(Spider):
    name = 'movie_comment'
    allowed_domains = ['movie.douban.com']
    sql = "SELECT douban_id FROM movies WHERE douban_id NOT IN (SELECT DISTINCT douban_id FROM comments)"
    cursor.execute(sql)
    movies = cursor.fetchall()
    random.shuffle(movies)
    start_urls = {
        str(i['douban_id']): ('https://movie.douban.com/subject/%s/comments?status=P' % i['douban_id']) for i in movies
    }

    def start_requests(self):
        print("Start URLs: ", self.start_urls)
        for key, url in self.start_urls.items():
            time.sleep(random.uniform(0, 1))  # 随机延迟请求，防止被封
            bid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(11))
            cookies = {
                'bid': bid,
            }
            headers = {
                'User-Agent': random.choice([
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
                ]),
                'Referer': 'https://movie.douban.com/',
                'Accept-Language': 'zh-CN,zh;q=0.9',
            }
            yield Request(url, cookies=cookies, headers=headers, meta={'main_url': url})

    def parse(self, response):
        main_url = response.meta['main_url']
        response_url = response.url
        print(f"Response URL: {response_url}, Status: {response.status}")

        if response.status == 404:
            print("Page not found: ", response.url)
            return

        douban_id = main_url.split("subject/")[1].split("/")[0]
        next_url = response.xpath('//a[@class="next"]/@href').extract()
        comment_item_list = response.xpath('//div[contains(@class, "comment-item")]').extract()

        print(f"Douban ID: {douban_id}, Comments Found: {len(comment_item_list)}")

        for resp_item in comment_item_list:
            resp_item = etree.HTML(resp_item)
            url_list = resp_item.xpath('//div[@class="avatar"]/a/@href')
            username_list = resp_item.xpath('//div[@class="avatar"]/a/@title')
            avator_list = resp_item.xpath('//div[@class="avatar"]/a/img/@src')
            vote_list = resp_item.xpath('//span[@class="votes"]/text()')
            rating_list = resp_item.xpath('//span[contains(@class,"allstar")]/@class')
            comment_time_list = resp_item.xpath('//span[contains(@class,"comment-time")]/@title')
            comment_list = resp_item.xpath('//span[@class="short"]/text()')
            comment_id_list = resp_item.xpath('//input/@value')

            comment = Comment()
            comment['douban_id'] = douban_id
            comment['douban_comment_id'] = comment_id_list[0] if comment_id_list else ""
            comment['douban_user_nickname'] = username_list[0] if username_list else ""
            comment['douban_user_avatar'] = avator_list[0] if avator_list else ""
            comment['douban_user_url'] = url_list[0] if url_list else ""
            comment['content'] = comment_list[0] if comment_list else ""
            comment['votes'] = int(vote_list[0]) if vote_list else 0
            comment['rating'] = rating_list[0] if rating_list else ""
            comment['comment_time'] = comment_time_list[0] if comment_time_list else ""
            yield comment

        if next_url:
            time.sleep(random.uniform(0, 1))  # 随机延迟请求
            next_page = "https://movie.douban.com/subject/%s/comments%s" % (douban_id, next_url[0])
            print("Next Page: ", next_page)
            bid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(11))
            cookies = {
                'bid': bid,
            }
            headers = {
                'User-Agent': random.choice([
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
                ]),
                'Referer': main_url,
                'Accept-Language': 'zh-CN,zh;q=0.9',
            }
            yield Request(next_page, cookies=cookies, headers=headers, meta={'main_url': main_url})