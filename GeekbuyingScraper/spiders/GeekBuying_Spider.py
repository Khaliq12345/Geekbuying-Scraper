import scrapy
from ..items import GeekbuyingscraperItem

class GeekBuyingSpider(scrapy.Spider):
    name = 'GeekBuying'
    start_urls = ['https://www.geekbuying.com/category/TV-Boxes---Mini-PCs-505/']

    def parse(self, response):
        items = GeekbuyingscraperItem()
        
        products = response.css('.view_items')
        for product in products:
            title = product.css('.pro_title::text').extract_first().strip()
            price = product.css('div.price::text').extract_first().strip()
            review = product.css('span.review_num::text').extract_first().strip()
            like = product.css('span.favite_count::text').extract_first().strip()
            image = product.css('img.lazy_img::attr(data-original)').get()
            image = 'https:' + image
            link = product.css('.pro_title::attr(href)').get()
            item_id = product.css('.pro_title::attr(id)').get()
            category = product.css('.pro_title::attr(category)').get()

            items['title'] = title
            items['price'] = price
            items['review'] = review
            items['like'] = like
            items['image'] = image
            items['link'] = link
            items['item_id'] = item_id
            items['category'] = category

            yield items

        next_page = response.css('.next::attr(href)').get()

        if next_page:
            yield response.follow(next_page, callback = self.parse)
        


