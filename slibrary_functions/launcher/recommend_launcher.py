# how to recommend
# if mouse press
# lb_recommend_temp
# lb_recommend_cg
# lb_recommend_cgn

# if request with cookie, then will return bMosaicBox with many div in it
# those div contain many book data
# if request with no cookie, then will return bMosaicBox with no div in it
# the way to solve when with no cookie, is use regular expression to get book url

from utils.common.circle import circle
from sszp.sszpThread import sszpThread
from value.strings import Recommend_Cookies

def recommend_launcher(self):
    self.recommend_cookie_idx = circle(self.recommend_cookie_idx, len(Recommend_Cookies))
    self.ln(f'start to get recommended books: cookie in pool index: {self.recommend_cookie_idx}')
    sszpThread(func=lambda: inner_recommend_launcher(self)).start()

def inner_recommend_launcher(self):
    books = self.recommend()
    self.signal_append_recommend.signal_append_recommend.emit(books)