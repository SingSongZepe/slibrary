import requests
from urllib.parse import urljoin as uj
from os.path import join as j
from bs4 import BeautifulSoup as bs
from datetime import datetime

from object.book import Book
from object.time import Time
from object.download import Download
from value.strings import *
from value.value import *
from utils.common.num_length_info import num_length_info

def download(self, book: Book):
    self.ln(f'start to download book: {book.title}')

    for i in range(self.cookie_from, len(Cookies)):
        book_headers = {
            'User-Agent': User_Agent,
            'Cookie': Cookies[i]
        }
        book_req = requests.get(book.url, headers=book_headers, verify=self.verify)
        if book_req.status_code != 200:
            self.le('book_req status code: ' + book_req.status_code)
            continue
        book_soup = bs(book_req.text, lxml_)

        download_hrefs = book_soup.select('.dlButton')
        if len(download_hrefs) == 0:
            self.le('book download path not found')
            continue
        download_href = download_hrefs[0]['href']
        download_url = uj(zlibrary_root_web, download_href)

        download_headers = {
            'User-Agent': User_Agent,
            'Cookie': Cookies[i],
        }

        download_req = requests.get(download_url, headers=download_headers, verify=self.verify)
        
        if download_req.status_code != 200:
            self.le('download_req status code: ' + download_req.status_code)
            continue
        
        # checking whether the book is a html
        if num_length_info(book.length) > unfair_limit and len(download_req.text) < unfair_limit:
            self.lw('recent account download is limit up, changing to anthor account')
            # if all the cookies are used to limit download
            if i == len(Cookies) - 1:
                return False
            continue
            
        # if program run to there, then downloaded yet
        with open(j(self.dp, book.title+'.'+ book.extension), 'wb') as pf:
            pf.write(download_req.content)

        now = datetime.now()

        
        self.ln(f'download book completely: {book.title}.{book.extension}, length: {book.length}')
        
        # after download set the cookie from
        self.cookie_from = i

        return Download(
            time=Time(now.year, now.month, now.day, now.hour, now.minute, now.second),
            book=book,
        )
        

        
