from scrapy.spiders import Spider
from scrapy.selector import Selector
from items import JobItem
from scrapy.http import Request
from models import SearchTerms
from datetime import datetime

class LeverSpider(Spider):
    name = "lever"
    allowed_domains = ["google.com"]

    def search_query(self):
        search_terms = list(SearchTerms.objects.all())
        query_items = []
        for term in search_terms:
            query_items.append(str(term))

        query = "q=site:jobs.lever.co+{}&tbs=qdr:m".format("+".join(query_items))
        return query

    def start_requests(self):
        search_query = self.search_query()
        base_url = "https://www.google.com/search?"
        start_urls = []

        start_urls.append(base_url + search_query)

        return [Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        """Extract job detail urls from response."""
        hxs = Selector(response)
        urls = hxs.xpath('//div[contains(@class, "r")]/a/@href').extract()
        for url in urls:
            url = url.replace("/url?q=", "")
            url = url.split("&")[0]
            print(url)
            yield Request(url, callback=self.parse_detail_pages, dont_filter=True)
            print(url)

    def parse_detail_pages(self, response):
        hxs = Selector(response)
        jobs = hxs.xpath('//div[contains(@class, "content")]')
        items = []
        for job in jobs:
            item = JobItem()
            item["title"] = job.xpath('//div[contains(@class, "posting-headline")]/h2/text()').extract_first()
            item["company"] = job.xpath('//div[contains(@class, "main-footer-text page-centered")]/p/a/text()').extract()
            item["company_url"] = job.xpath('//div[contains(@class, "main-footer-text page-centered")]/p/a/@href').extract()
            item["body"] = job.xpath('//div[contains(@class, "section page-centered")]').extract()
            item["location"] = job.xpath('//div[contains(@class, "sort-by-time posting-category medium-category-label")]').extract_first()
            item["url"] = response.request.url
            item["pub_date"] = str('n/a')
            item["email"] = str('n/a')
            item["salary"] = str('n/a')
            item["scrape_date"] = datetime.now()
            item["job_board"] = "Lever"
            item["board_url"] = "lever.co"
            items.append(item)
        return items
