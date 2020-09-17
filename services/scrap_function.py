import sys

import requests
from bs4 import BeautifulSoup

from config import configs
from core import prefixy
from interfaces import discovers


class ScrapFunction(discovers.Discoverer, prefixy.Prefixy):

    def __init__(self, url):
        super().__init__("COVID-19", {})
        self.url = url

    # Our Repo for news content
    def page_loader(self) -> dict:
        global art, con
        try:
            page_requested = requests.get(self.url)
            print("Status Code.....")
        except Exception:
            print("Url not Active anymore....")
            sys.exit("Crashed....")

        print(page_requested.status_code)
        print("Fetching Content....")

        soup = BeautifulSoup(page_requested.content, configs.parser)
        print("SPAN TAG_______________________")
        try:
            spantag = soup.find_all('span', itemprop="headline")
            con = ">".join([p.text for p in spantag])
            print(con)
        except AttributeError:
            print("Attribute Error..")
            pass
        print("Article Body___________________")
        try:
            articlebody = soup.find_all('div', itemprop="articleBody")
            art = ">".join([x.text for x in articlebody])
            print(art)
        except AttributeError:
            pass
        articlebody_list = art.split(">")
        spantag_list = con.split(">")
        article_map = dict(zip(spantag_list, articlebody_list))
        print(article_map)
        for itr in article_map:
            print(itr.upper(), ":", article_map[itr])
            print("\n")
        return article_map
