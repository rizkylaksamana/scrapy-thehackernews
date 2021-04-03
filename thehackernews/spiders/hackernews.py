import scrapy
import json


class HackernewsSpider(scrapy.Spider):
    name = 'hackernews'
    allowed_domains = ['thehackernews.com']
    start_urls = ['https://thehackernews.com/search/label/data%20breach/']

    def parse(self, response):
        for post in response.css('div.body-post'):
            yield{
                'title': post.css('.clear.home-right h2::text').get(),
                'date': post.css('.clear.home-right div::text').get(),
                'author': post.css('.clear.home-right span::text').re(r'\w* \w*'),
                'link': post.css('.body-post a::attr(href)').get()
            }

        for a in response.css('a.blog-pager-older-link-mobile::attr(href)'):
                    yield response.follow(a, callback=self.parse)
