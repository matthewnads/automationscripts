"""
WebScraper to Find emails from sites using a DF from a google doc.
"""
import scrapy
import logging
import os
import pandas as pd
import re
from scrapy.crawler import CrawlerProcess

col_list = ['FARM / ORGANIZATION', 'WEBSITE / ABOUT']
NPsheet = pd.read_csv('C:/Users/matth/Downloads/NPsheet.csv', header=2, usecols=col_list)
NPsheet = NPsheet.dropna(subset=['FARM / ORGANIZATION'])

websites = []
emails = []
organizations = []

def organization(item):
    organizations.append(item)

def websiteFunction(item):
    websites.append(item)

NPsheet['FARM / ORGANIZATION'].map(organization)
NPsheet['WEBSITE / ABOUT'].map(websiteFunction)


class MailSpider(scrapy.Spider):
    name = 'emails'
    start_urls = websites

    def parse(self, response):
        for link in websites:
            yield scrapy.Request(url=link, callback=self.parse_link)

    def parse_link(self, response):
        for word in self.reject:
            if word in str(response.url):
                return

        html_text = str(response.text)
        mail_list = re.findall("\w+@\w+\.{1}\w+", html_text)
        dic = {'email': mail_list, 'link': str(response.url)}
        df = pd.DataFrame(dic)
        print(df)

test = MailSpider(websites)
test.parse(websites)
test.parse_link(websites)
