# this function will return a book widget 
# for searching and recommending

from value.value import *
from value.strings import *
from value.font import *
from value.color import *
from object.book import Book
from utils.common.load_pic import load_pic
from sszp.sszpThread import sszpThread

from PySide6.QtWidgets import QLabel, QWidget, QTextEdit, QFrame
from PySide6.QtGui import QCursor, QFont
from PySide6.QtCore import Qt

def wgt_book(self, book: Book) -> QWidget:
    width = self.book_item.width     # left padding 5 right padding 15
    height = self.book_item.height   # top padding 5 bottom padding 5
    pic_x = self.book_item.pic_x
    pic_y = self.book_item.pic_y
    pic_width = self.book_item.pic_width
    pic_height = self.book_item.pic_height
    
    # a book item
    wgt_main = QWidget() # pic 3 * 5
    wgt_main.setFixedWidth(width)
    wgt_main.setFixedHeight(height)
    wgt_main.setGeometry(ax, ay, width, height)
    wgt_main.setStyleSheet(f'''background: {self.book_item.background};
                            border-radius: {self.book_item.border_radius}px;''')
    # dry(wgt_main, 'blue')

    wgt_pic = QWidget(wgt_main)
    wgt_pic.setGeometry(pic_x, pic_y, pic_width, pic_height)
    
    lb_pic = QLabel(wgt_pic)
    lb_pic.setGeometry(pic_x, pic_y, pic_width, pic_height)
    lb_pic.setScaledContents(True)
    lb_pic.setCursor(QCursor(Qt.PointingHandCursor))
    # use a thread to load pic
    load_pic(lb_pic, book.cover)
    # sszpthread = sszpThread(func=lambda: load_pic(lb_pic, book.cover))
    # sszpthread.start()

    # lb_pic clicked event
    lb_pic.mousePressEvent = lambda eve: self.download_launcher(book)

    # title
    wgt_title = QWidget(wgt_main)
    wgt_title.setGeometry(self.book_item.title_x, self.book_item.title_y, self.book_item.title_width, self.book_item.title_height)
    
    te_title = QTextEdit(wgt_title)
    te_title.setGeometry(self.book_item.te_title_x, self.book_item.te_title_y, self.book_item.te_title_width, self.book_item.te_title_height)
    te_title.setText(book.title)
    te_title.setReadOnly(True)
    te_title.setFrameShape(QFrame.Shape.NoFrame)
    te_title.setFontFamily(times_)
    te_title.setFontPointSize(12)
    te_title.setCursor(QCursor(Qt.PointingHandCursor))
    # te_title clicked event
    # te_title.mousePressEvent = lambda eve: self.download_launcher(book) 

    # press
    wgt_press = QWidget(wgt_main)
    wgt_press.setGeometry(self.book_item.press_x, self.book_item.press_y, self.book_item.press_width, self.book_item.press_height)

    lb_press = QLabel(wgt_press)
    lb_press.setGeometry(self.book_item.lb_press_x, self.book_item.lb_press_y, self.book_item.lb_press_width, self.book_item.lb_press_height)
    lb_press.setText(book.press)
    font = QFont()
    font.setFamily(times_)
    lb_press.setStyleSheet(f'''color: {color_press};
                            padding-left: 10px;
                            font-size: 12px;''')
    lb_press.setFont(font)

    # author
    wgt_author = QWidget(wgt_main)
    wgt_author.setGeometry(self.book_item.author_x, self.book_item.author_y, self.book_item.author_width, self.book_item.author_height)

    lb_author = QLabel(wgt_author)
    lb_author.setGeometry(self.book_item.lb_author_x, self.book_item.lb_author_y, self.book_item.lb_author_width, self.book_item.lb_author_height)
    lb_author.setText(book.author)
    lb_author.setStyleSheet(f'''padding-left: 15px;
                            font-size: 12px;
                            font-style: italic;
                            color: {color_author};
                            width: 80%;
                            ''')
    lb_press.setFont(font)

    # info
    wgt_info = QWidget(wgt_main)
    wgt_info.setGeometry(self.book_item.info_x, self.book_item.info_y, self.book_item.info_width, self.book_item.info_height)
    font.setPointSize(8)

        # lb_language
    lb_language = QLabel(wgt_info)
    lb_language.setGeometry(self.book_item.language_x, self.book_item.language_y, self.book_item.language_width, self.book_item.language_height)
    lb_language.setText(book.language)
    lb_language.setAlignment(Qt.AlignmentFlag.AlignCenter)
    lb_language.setFont(font)

        # v-line 1
    vline1 = QFrame(wgt_info)
    vline1.setGeometry(self.book_item.vline1_x, self.book_item.vline1_y, self.book_item.vline1_width, self.book_item.vline1_height)
    vline1.setFrameShape(QFrame.Shape.VLine)
    vline1.setFrameShadow(QFrame.Shadow.Sunken)

        # lb_year
    lb_year = QLabel(wgt_info)
    lb_year.setGeometry(self.book_item.year_x, self.book_item.year_y, self.book_item.year_width, self.book_item.year_height)
    lb_year.setText(book.year)
    lb_year.setAlignment(Qt.AlignmentFlag.AlignCenter)
    lb_year.setFont(font)
        # v-line 2
    vline2 = QFrame(wgt_info)
    vline2.setGeometry(self.book_item.vline2_x, self.book_item.vline2_y, self.book_item.vline2_width, self.book_item.vline2_height)
    vline2.setFrameShape(QFrame.Shape.VLine)
    vline2.setFrameShadow(QFrame.Shadow.Sunken)

        # lb_ext_len
    lb_ext_len = QLabel(wgt_info)
    lb_ext_len.setGeometry(self.book_item.ext_len_x, self.book_item.ext_len_y, self.book_item.ext_len_width, self.book_item.ext_len_height)
    lb_ext_len.setText(f'{book.extension}, {book.length}')
    lb_ext_len.setAlignment(Qt.AlignmentFlag.AlignCenter)
    lb_ext_len.setFont(font)

    return wgt_book
