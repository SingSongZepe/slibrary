
from slibrary_ui import Ui_MainWindow
from object.book_item import Book_Item
from object.history_item import hSearch_Item, hBook_Item
from object.slibrary import Slibrary
from value.strings import *
from value.pic_path import *
from value.value import *
from value.color import *
from signal_.signal_append_book import SIGNAL_APPEND_BOOK
from signal_.signal_append_history import SIGNAL_APPEND_HISTORY
from signal_.signal_append_recommend import SIGNAL_APPEND_RECOMMEND
from utils.common.dry import dry

from PySide6.QtWidgets import QMainWindow, QScrollArea, QWidget, QGridLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QMutex, Qt

class SLIBRARY(QMainWindow, Ui_MainWindow):

    # ! event
        # drag
    from event.drag.mouse_move_event import mouseMoveEvent
    from event.drag.mouse_press_event import mousePressEvent
    from event.drag.mouse_release_event import mouseReleaseEvent
        # close
    from event.close_event import closeEvent

    # ! slibrary_functions
        # launcher
    from slibrary_functions.launcher.search_launcher import search_launcher, search_launcher_not_append
    from slibrary_functions.launcher.download_launcher import download_launcher, download_launcher_not_append
    from slibrary_functions.launcher.append_history_launcher import append_history_search_launcher, append_history_book_launcher
    from slibrary_functions.launcher.recommend_launcher import recommend_launcher
        # function
    from slibrary_functions.function.search import search
    from slibrary_functions.function.download import download
    from slibrary_functions.function.recommend import recommend

    # from slibrary_functions.other_init import __other_init__
    from slibrary_functions.toggle import toggle
    from slibrary_functions.toggle_history import toggle_history
    from slibrary_functions.hover import hover, hover_out
    from slibrary_functions.append_book import append_book
    from slibrary_functions.append_books import append_books
    from slibrary_functions.append_history import append_history_book, append_history_search
    from slibrary_functions.append_recommend import append_recommend
    from slibrary_functions.append_recommends import append_recommends

    # ! windows
    from windows.wgt_book import wgt_book

    # ! utils
    from utils.slibrary.logger import ln, lw, le, log_file
    from utils.slibrary.clear_history import clear_history
        # read and save
    from utils.slibrary.read import read
    from utils.slibrary.save import save
    from utils.slibrary.setup import setup

    def __init__(self) -> None:
        super(SLIBRARY, self).__init__()

        self.setupUi(self)
        self.setWindowTitle(title_mainwindow)
        self.setWindowIcon(QPixmap(pic_path_sszp))
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.mutex = QMutex()

        self.__other_init__()

    def __other_init__(self):
        
        # fro dragging
        self.isMousePressed = False
        self.mousePressPos = None
        
        # ! icon init
            # slibrary
        self.lb_slibrary.setPixmap(QPixmap(pic_path_slibrary))
            # tab
        self.lb_wgt_home.setPixmap(QPixmap(pic_path_home))  
        self.lb_wgt_home.setScaledContents(True)
        self.lb_wgt_search.setPixmap(QPixmap(pic_path_search))
        self.lb_wgt_search.setScaledContents(True)
        self.lb_wgt_recommend.setPixmap(QPixmap(pic_path_recommend))
        self.lb_wgt_recommend.setScaledContents(True)
        self.lb_wgt_history.setPixmap(QPixmap(pic_path_history))
        self.lb_wgt_history.setScaledContents(True)
        self.lb_wgt_setting.setPixmap(QPixmap(pic_path_setting))
        self.lb_wgt_setting.setScaledContents(True)
            # bar
        self.lb_minimize.setPixmap(QPixmap(pic_path_minimize))
        self.lb_minimize.setScaledContents(True)
        self.lb_full.setPixmap(QPixmap(pic_path_full))
        self.lb_full.setScaledContents(True)
        self.lb_quit.setPixmap(QPixmap(pic_path_quit))
        self.lb_quit.setScaledContents(True)
            # wgt_main_history
        self.lb_history_book.setPixmap(QPixmap(pic_path_book))
        self.lb_history_book.setScaledContents(True)
        self.lb_history_search.setPixmap(QPixmap(pic_path_search))
        self.lb_history_search.setScaledContents(True)
        self.lb_history_clear.setPixmap(QPixmap(pic_path_clear))
        self.lb_history_clear.setScaledContents(True)

            # wgt_main_recommend
        self.lb_recommend_cg.setPixmap(QPixmap(pic_path_change))
        self.lb_recommend_cg.setScaledContents(True)
        self.lb_recommend_cgn.setPixmap(QPixmap(pic_path_change))
        self.lb_recommend_cgn.setScaledContents(True)

        # ! signal
        self.signal_append_book = SIGNAL_APPEND_BOOK()
        self.signal_append_book.signal_append_book.connect(self.append_book)
        self.signal_append_book.signal_append_books.connect(self.append_books)
        self.signal_append_history = SIGNAL_APPEND_HISTORY()
        self.signal_append_history.signal_append_history_book.connect(self.append_history_book_launcher)
        self.signal_append_history.signal_append_history_search.connect(self.append_history_search_launcher)
        self.signal_append_recommend = SIGNAL_APPEND_RECOMMEND()
        self.signal_append_recommend.signal_append_recommend.connect(self.append_recommends)

        # ! label
            # bar
        self.lb_quit.mousePressEvent = lambda eve: self.close()
        self.lb_minimize.mousePressEvent = lambda eve: self.showMinimized()

            # toggle tab
                # press
        self.lb_wgt_home.mousePressEvent = lambda eve: self.toggle(home_)
        self.lb_wgt_search.mousePressEvent = lambda eve: self.toggle(search_)
        self.lb_wgt_recommend.mousePressEvent = lambda eve: self.toggle(recommend_)
        self.lb_wgt_history.mousePressEvent = lambda eve: self.toggle(history_)
        self.lb_wgt_setting.mousePressEvent = lambda eve: self.toggle(setting_)
                # hover
        self.lb_wgt_home.enterEvent = lambda eve: self.hover(home_)
        self.lb_wgt_search.enterEvent = lambda eve: self.hover(search_)
        self.lb_wgt_recommend.enterEvent = lambda eve: self.hover(recommend_)
        self.lb_wgt_history.enterEvent = lambda eve: self.hover(history_)
        self.lb_wgt_setting.enterEvent = lambda eve: self.hover(setting_)
                # hover_out
        self.lb_wgt_home.leaveEvent = lambda eve: self.hover_out(home_)
        self.lb_wgt_search.leaveEvent = lambda eve: self.hover_out(search_)
        self.lb_wgt_recommend.leaveEvent = lambda eve: self.hover_out(recommend_)
        self.lb_wgt_history.leaveEvent = lambda eve: self.hover_out(history_)
        self.lb_wgt_setting.leaveEvent = lambda eve: self.hover_out(setting_)

            # history toggle
        self.lb_history_search.mousePressEvent = lambda eve: self.toggle_history(history_search_)
        self.lb_history_book.mousePressEvent = lambda eve: self.toggle_history(history_book_)
                # history clear
        self.lb_history_clear.mousePressEvent = lambda eve: self.clear_history()

            # recommend
        self.lb_recommend_temp.mousePressEvent = lambda eve: self.recommend_launcher()
        self.lb_recommend_cg.mousePressEvent = lambda eve: self.recommend_launcher()
        self.lb_recommend_cgn.mousePressEvent = lambda eve: self.recommend_launcher()

        # ! pushButton
        self.pb_search.clicked.connect(self.search_launcher)

        # ! lineEdit
        self.le_search.returnPressed.connect(self.search_launcher)
        
        # ! value init
        self.lb_selected = {
            home_: self.lb_home_selected,
            search_: self.lb_search_selected,
            recommend_: self.lb_recommend_selected,
            history_: self.lb_history_selected,
            setting_: self.lb_setting_selected,
        }
        self.wgt_mains = {
            home_: self.wgt_main_home,
            search_: self.wgt_main_search,
            recommend_: self.wgt_main_recommend,
            history_: self.wgt_main_history,
            setting_: self.wgt_main_setting,
        }
        self.lb_histories = {
            history_search_: self.lb_history_search,
            history_book_: self.lb_history_book,
        }
        self.wgt_histories = {
            history_search_: self.wgt_history_search,
            history_book_: self.wgt_history_book,
        }
            # ! the data will be loaded from the cache

        # read the data from file and give it to vars
        # and then it is needed to init the ui of program
        # ? maybe a better way to do this is store those data in a var of slibrary
        # ? self.slibrary, where slibrary is a instance of object.slibrary.Slibrary
        # ? and it will hold all data that is needed to store
        # ? in this way, when maintain the program, if you want to add a new var,
        # ? then you need only add a new var to the object
        # ? not the hole program in init function
        # slibrary: Slibrary = self.read()
        
        self.current_type = home_  # for main toggle
        self.current_history_type = history_search_  # for history toggle
        self.verify = True
        self.dp = ''
        self.cookie_from = 0    # from which cookie to attempt to download a book 
        self.searches = []      # [object.history_search.History_Search]
        self.downloads = []     # [object.download.Download]
        self.recommend_cookie_idx = 0

            # book item (size) for showing of book for search result showing
        book_width = self.wgt_result.width() // columns - 2 * (columns - 1) * spacing_gl_result
        book_height = height_book_item
            # search item (size) for showing of search for history_search showing
        history_width = self.wgt_history_search.width() // history_columns -  2 * (history_columns - 1) * spacing_gl_history
        history_height = height_history_item
            # book item (size) for showing of book for history_book showing

        self.book_item = Book_Item(
            width=book_width,
            height=book_height,
            border_radius=book_item_radius,
            background=color_basic_deep,
        )
        self. search_item = hSearch_Item(
            x=0,
            y=0,
            w=history_width,
            h=history_height,
            br=history_item_radius,
            bg=color_basic_deep,
        )
        # hbook_item if for history book item
        self.hbook_item = hBook_Item(
            x=0,
            y=0,
            w=history_width,
            h=history_height,
            br=history_item_radius,
            bg=color_basic_deep,
        )

        # ! widget init 
        self.wgt_main_search.setVisible(False)
        self.wgt_main_recommend.setVisible(False)
        self.wgt_main_history.setVisible(False)
        self.wgt_main_setting.setVisible(False)

            # for self.wgt_result scroll
            # sa is scrollArea for shor
        self.sa_result = QScrollArea(self.wgt_result)
        self.sa_result.setWidgetResizable(True)
        self.sa_result.setGeometry(0, 0, self.wgt_result.width(), self.wgt_result.height())
        # dry(self.sa_result, 'red') # for testing

        # in scrollArea, a wgt is need for scrolling
        self.wgt_for_sa_result = QWidget()  
        self.sa_result.setWidget(self.wgt_for_sa_result)

        self.gl_result = QGridLayout()
        self.wgt_for_sa_result.setLayout(self.gl_result)
            # for wgt.wgt_history_search scroll
        self.sa_history_search = QScrollArea(self.wgt_history_search)
        self.sa_history_search.setWidgetResizable(True)
        self.sa_history_search.setGeometry(0, 0, self.wgt_history_search.width(), self.wgt_history_search.height())

        self.wgt_for_sa_history_search = QWidget()
        self.sa_history_search.setWidget(self.wgt_for_sa_history_search)

        self.gl_history_search = QGridLayout()
        self.wgt_for_sa_history_search.setLayout(self.gl_history_search)
            # for wgt.wgt_history_book scroll
        self.sa_history_book = QScrollArea(self.wgt_history_book)
        self.sa_history_book.setWidgetResizable(True)
        self.sa_history_book.setGeometry(0, 0, self.wgt_history_book.width(), self.wgt_history_book.height())

        self.wgt_for_sa_history_book = QWidget()
        self.sa_history_book.setWidget(self.wgt_for_sa_history_book)

        self.gl_history_book = QGridLayout()
        self.wgt_for_sa_history_book.setLayout(self.gl_history_book)
            # for wgt.wgt_recommend scroll
        self.sa_recommend_book = QScrollArea(self.wgt_recommend_book)
        self.sa_recommend_book.setWidgetResizable(True)
        self.sa_recommend_book.setGeometry(0, 0, self.wgt_recommend_book.width(), self.wgt_recommend_book.height())

        self.wgt_for_sa_recommend_book = QWidget()
        self.sa_recommend_book.setWidget(self.wgt_for_sa_recommend_book)

        self.gl_recommend_book = QGridLayout()
        self.wgt_for_sa_recommend_book.setLayout(self.gl_recommend_book)

        # hide result
        self.wgt_result.setVisible(False)
        self.wgt_history_book.setVisible(False)
