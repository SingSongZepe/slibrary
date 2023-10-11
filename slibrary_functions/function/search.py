import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin as uj

from object.search import Search
from object.history_search import History_Search
from object.book import Book
from value.strings import *
from value.value import *
from utils.common.retitle import retitle

def search(self, search: Search) -> History_Search:
    params = {
    }   
    if search.year_from:
        params[year_from_] = search.year_from
    if search.year_to:
        params[year_to_] = search.year_to
    if search.languages:
        params[languages_] = search.language
    if search.extensions:
        params[extensions_] = search.extensions
    if search.exact_matching:
        params[exact_matching_] = search.exact_matching

    if search.search_type == general_:
        main_url = zlibrary_search_web + search.q
    else:
        main_url = zlibrary_search_full_web + search.q
    
    main_req = requests.get(main_url, params=params, verify=self.verify)
    if main_req.status_code != 200:
        self.le(f'main_req status code: {main_req.status_code}')
        return
    
    # parse
    main_soup = bs(main_req.text, lxml_)
    tr_books = main_soup.select('.bookRow')

    # use to store book info (object.book.Book)
    books = []
    main_cover = '' # for history search showing
    for tr_book in tr_books[:search.book_nums]: # download nums
        a_book = tr_book.select('h3 a')[0]

        # book href / url
        href_book = a_book['href']
        url_book = uj(zlibrary_root_web, href_book)
        
        # book cover
        # img tag in string view as follows:
        # <img alt="" class="cover lazy" data-src="https://static.zlibrary-africa.se/covers100/books/3c/a2/40/3ca240f4b4b318dce71984fce8238c25.jpg" data-srcset="https://static.zlibrary-africa.se/covers100/books/3c/a2/40/3ca240f4b4b318dce71984fce8238c25.jpg 1x, https://static.zlibrary-africa.se/covers200/books/3c/a2/40/3ca240f4b4b318dce71984fce8238c25.jpg 2x"/>
        cover_book = tr_book.select('img.lazy')[0]['data-src']
        if main_cover == '':
            main_cover = cover_book

        # book title
        title_book = retitle(a_book.text)

        # book press 
        press_book = tr_book.select('td td div a')[0].text if tr_book.select('td td div a')[0].text else 'press: unknown'

        # book author
        author_book = tr_book.select('.authors a')[0].text if tr_book.select('.authors a')[0].text else 'author: unknown'

        # year info (perhaps not exists)
        year_book = 'unknown'
        div_year_book = tr_book.select('.bookDetailsBox .property_year .property_value')
        if len(div_year_book) != 0:
            year_book = div_year_book[0].text

        # language info
        language_book = 'unknown'
        div_language_book = tr_book.select('.bookDetailsBox .property_language .property_value')
        if len(div_language_book) != 0:
            language_book = div_language_book[0].text

        # property__file  file size and extension info
        info_book = 'unknown, 0 KB'
        div_info_book = tr_book.select('.bookDetailsBox .property__file .property_value')
        if len(div_info_book) != 0:
            info_book = div_info_book[0].text
        extension_info, length_info = info_book.split(',')

        books.append(Book(
            url=url_book, 
            cover=cover_book , 
            title=title_book, 
            press=press_book, 
            author=author_book, 
            year=year_book, 
            language=language_book, 
            extension=extension_info, 
            length=length_info
        ))

    self.signal_append_book.signal_append_books.emit(books)

    # show it to the history view
    return History_Search(
        search=search,
        cover=main_cover, # cover from first searched book
    )

