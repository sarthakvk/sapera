import json
import os

import scrapy
from scrapy.crawler import CrawlerProcess

from sapera.settings import BASE_DIR


def make_algo_obj(algo_tag, algo_type):
    return dict(
        link=algo_tag.xpath("@href").get(),
        name=algo_tag.xpath("text()").get(),
        algo_type=algo_type,
    )


class MySpider(scrapy.Spider):
    name = "MySpider"

    start_urls = [
        "https://github.com/TheAlgorithms/Python/blob/master/DIRECTORY.md",
    ]

    def parse(self, response):
        filename = BASE_DIR + "/data/.list-of-algorithms.json"
        algo_types_list_xpath = "//div[@id='readme']/*/h2/text()"

        algo_class = list(response.xpath(algo_types_list_xpath).getall())
        data = {}

        for indx, algo_type in enumerate(algo_class):
            algo_type_xpath = "//div[@id='readme']/*/ul[{indx}]/li//a".format(
                indx=indx + 1)
            data[algo_type] = [
                make_algo_obj(algo_tag, algo_type)
                for algo_tag in response.xpath(algo_type_xpath)
            ]
        with open(BASE_DIR + "/sapera/scraper/status.txt", "w") as status:
            try:
                with open(filename, "r+") as f:
                    try:
                        if json.load(f) != data:
                            f.write(json.dumps(data, indent=4))
                            status.write("Updated")
                        else:
                            status.write("Already upto Date!")
                    except:
                        f.write(json.dumps(data, indent=4))
                        status.write("Updated")
            except:
                with open(filename, "w") as f:
                    f.write(json.dumps(data, indent=4))
                    status.write("Updated")


process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {
            "format": "json"
        },
    },
})

if __name__ == "__main__":
    process.crawl(MySpider)
    process.start()
