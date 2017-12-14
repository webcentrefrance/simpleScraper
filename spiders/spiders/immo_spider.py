#!/usr/bin/python
import scrapy

class QuotesSpider(scrapy.Spider):
	name = "scrap"

	def start_requests(self):
		with open("urls.txt", "r") as f:
			urls = [url.strip() for url in f.readlines()]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		title = response.css('.someclass').extract()
		appart = response.css('.someotherclass').extract()
		maison = response.css('.oneanotherclass').extract()

		for item in zip(title, appart, maison):
			scraped_info = {
				'title': item[0].strip(),
				'description': item[1].strip(),
				'random': item[2].strip()
			}

			yield scraped_info