from datetime import datetime

from object.book import Book
from object.time import Time
from object.download import Download
from sszp.sszpThread import sszpThread

def download_launcher(self, book: Book):
    now = datetime.now()
    self.downloads.append(Download(
        time=Time(
            now.year, now.month, now.day, now.hour, now.minute, now.second,
        ),
        book=book,
    ))

    sszpThread(lambda: inner_downlaod(self, book=book)).start()

# use for download_launcher for thread download
# avoid from blocking the main thread
# use for requesting
def inner_downlaod(self, book):
    download = self.download(book)
    
    # after getting download
    # then append it to history
    if download:
        self.signal_append_history.signal_append_history_book.emit(download)
    else:
        self.le('all cookie are used up, add new cookie to the pool or waiting for tomorrow')

def download_launcher_not_append(self, book: Book):
    sszpThread(func=lambda: self.download(book)).start()

