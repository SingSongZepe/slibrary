import requests
import re
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin as uj

from utils.common.collect_book_info import collect_book_info
from value.strings import *
from value.value import *

def recommend(self):
    recommend_headers = {
        User_Agent_ : User_Agent,
        Connection_: Connection,
        Cookie_: Recommend_Cookies[self.recommend_cookie_idx],
    }

    recommend_req = requests.get(zlibrary_root_web, headers=recommend_headers, verify=self.verify)
    if recommend_req.status_code != 200:
        self.ln(f'recommend_req failed, status code: {recommend_req.status_code}')
        return

    recommend_soup = bs(recommend_req.text, lxml_)
    scripts = recommend_soup.find_all(script_)
    if len(scripts) > 14:
        script = scripts[14].text
    else:
        self.ln('script that contain info not found')
        return
    # title_pattern = r'"title":\s?"(.*?)"'
    url_pattern = r'"url":\s?"(.*?)"'
    # pic_pattern = r'"cover":\s?"(.*?)"'
    # author_pattern = r'data-author=\s?\\"(.*?)\\"'

    # titles = re.findall(title_pattern, script)
    urls = re.findall(url_pattern, script)
    # pics = re.findall(pic_pattern, script)
    # authors = re.findall(author_pattern, script)
    
    books = []
    for i in range(len(urls[:book_nums_default])):
        recommend_url = urls[i].replace('\\', '')
        recommend_url = uj(zlibrary_root_web, recommend_url)

        books.append(collect_book_info(recommend_url, self.verify))
    
    return books

def unicode2chinese(unicode_txt):
    return unicode_txt.encode('utf-8').decode('unicode_escape')
    