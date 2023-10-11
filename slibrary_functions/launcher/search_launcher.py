from datetime import datetime

from sszp.sszpThread import sszpThread
from object.search import Search
from object.time import Time
from object.history_search import History_Search
from value.strings import *
from value.value import *

def search_launcher(self, eve):
    # 
    self.q = self.le_search.text()
    if self.q == '' or self.q is None:
        self.lw('no search key word entered, please enter book you want download')
        return

    search_type = self.comb_search_type.currentText()
    # from year
    year_from = ''
    if self.cb_from_year.isChecked():
        year_from = self.le_from_year.text()
        self.ln('search setting year from: ' + year_from)
    else:
        self.ln('search setting year from: Any')
    
    # to year
    year_to = ''
    if self.cb_to_year.isChecked():
        year_to = self.le_to_year.text()
        self.ln('search setting yearTo: ' + year_to_)
    else:
        self.ln('search setting yearTo: Any')

    # languages
    languages = []
    if self.cb_languages.isChecked():
        # comb comboBox
        languages = self.comb_languages.currentText()
        self.ln('search setting languages: ' + languages)
    else:
        self.ln('search setting languages: Any')

    # extensions
    extensions = []
    if self.cb_extensions.isChecked():
        extensions = self.comb_extensions.currentText()
        self.ln('search setting extensions: ' + extensions)
    else:
        self.ln('search setting extensions: Any')

    # exact matching
    exact_matching = self.cb_exact_matching.isChecked()
    on_ = 'on'
    off_ = 'off'
    self.ln(f'search setting exact matching turn {on_ if exact_matching else off_}')

    # use to show some of the search result
    book_nums = book_nums_default
    if self.cb_book_nums.isChecked():
        book_nums = int(self.comb_book_nums.currentText())
        self.ln(f'search setting result book nums: {book_nums}')
    else:
        book_nums = book_nums_default
        self.ln(f'search setting result book nums: {book_nums_default}')

    now = datetime.now()
    search = Search(
        q=self.le_search.text(),
        time=Time(now.year, now.month, now.day, now.hour, now.minute, now.second),
        search_type=search_type,
        year_from=year_from if year_from else None,
        year_to=year_to if year_to else None,
        languages=languages if languages else [],
        extensions=extensions if extensions else [],
        exact_matching='1' if exact_matching else None,
        book_nums=book_nums,
    )

    history_search = self.search(search) # return History_Search
    if isinstance(history_search, History_Search):   
        self.searches.append(search) # append to history_search
        self.signal_append_history.signal_append_history_search.emit(history_search)
    else:
        self.le('error append search history, object not match')


def search_launcher_not_append(self, search: Search):
    # change the text of le_search
    self.le_search.setText(search.q)
    # then search
    sszpThread(func=lambda: self.search(search)).start()
