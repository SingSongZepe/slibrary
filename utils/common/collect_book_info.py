import requests
from bs4 import BeautifulSoup as bs
from utils.common.retitle import retitle

from value.strings import *
from utils.common.log_common import ln_c, lw_c, le_c
from object.book import Book

# url is zlibrary main url for getting info
def collect_book_info(url, verify=True) -> Book:
    book_headers = {
        User_Agent_: User_Agent,
        Connection_: Connection,
        Cookie_: Cookie_[0] # use any cookie that can assess to book info
    }

    book_req = requests.get(url, headers=book_headers, verify=verify)
    if book_req.status_code != 200:
        le_c('book info request failed')
        return
    book_soup = bs(book_req.text, lxml_)
    title = retitle(book_soup.find_all(attrs={'itemprop': 'name'})[0].text)
    author = book_soup.find_all(attrs={'itemprop': 'author'})[0].text

    cover = book_soup.select('.z-book-cover img')[0].get('src')
    t_year = book_soup.select('.property_year .property_value')
    if len(t_year) != 0:
        year = t_year[0].text
    else:
        year = 'unknown'
    t_press = book_soup.select('.property_publisher .property_value')
    if len(t_press) != 0:
        press = t_press[0].text
    else:
        press = 'unknown'
    t_lang = book_soup.select('.property_language .property_value')
    if len(t_lang) != 0:
        language = t_lang[0].text
    else:
        language = 'unknown'
    t_file = book_soup.select('.property__file .property_value')
    if len(t_file) != 0:
        extension, length = t_file[0].text.split(', ')
    else:
        extension = 'unknown'
        length = 'unknown'

    return Book(
        url=url,
        cover=cover,
        title=title,
        press=press,
        author=author,
        year=year,
        language=language,
        extension=extension,
        length=length
    )


