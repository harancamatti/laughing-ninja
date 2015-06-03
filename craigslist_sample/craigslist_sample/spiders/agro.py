#  coding: utf-8 --
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem


class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["www.agrolivros.com.br"]
    start_urls = ["http://www.agrolivros.com.br"]

    rules = (Rule (SgmlLinkExtractor(allow=(),restrict_xpaths=())
    , callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//html')
        items = []
        for titles in titles:
            if titles.select('/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/text()'):
                item = CraigslistSampleItem()
                item ["url"] = response.url
                item ["codigo"] = titles.xpath('/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/text()').extract()
                item ["description"] = titles.xpath('//meta[@name="description"]/@content').extract()
                item ["title"] = titles.xpath('/html/head/title/text()').extract()
                items.append(item)
        return(items)

