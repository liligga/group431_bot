import requests
from parsel import Selector
from pprint import pprint


class MashinaParser:
    MAIN_URL = "https://www.mashina.kg/search/all/"
    BASE_URL = "https://www.mashina.kg/"
    def get_page(self):
        response = requests.get(MashinaParser.MAIN_URL) # запрос страницы с сервера
        print(response.status_code) # сигнал о том, правильный ли URL
        # print(response.text[:350])
        self.page = response.text

    def get_page_title(self):
        html = Selector(text=self.page)
        title = html.css('title::text').get()
        print(title)

    def get_car_links(self):
        selector = Selector(text=self.page)
        links = selector.css('div.list-item a::attr(href)').getall()
        links = list(map(lambda l: f"{MashinaParser.BASE_URL}{l}", links))
        pprint(links)
        return links[:3]


if __name__ == "__main__":
    parser = MashinaParser()
    parser.get_page()
    # my_parser.get_page_title()
    parser.get_car_links()
