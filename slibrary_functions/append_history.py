
from value.font import *
from value.color import *
from object.download import Download
from object.history_search import History_Search
from sszp.sszpThread import sszpThread
from utils.common.load_pic import load_pic
from utils.common.open_url import open_url

from PySide6.QtWidgets import QWidget, QLabel, QComboBox, QTextEdit
from PySide6.QtCore import QMutexLocker, Qt
from PySide6.QtGui import QCursor, QFont, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QFrame

def append_history_book(self, download: Download, gx: int, gy: int):
    # append to history book
    
    wgt_main = QWidget()
    wgt_main.setFixedWidth(self.hbook_item.w)
    wgt_main.setFixedHeight(self.hbook_item.h)
    wgt_main.setGeometry(self.hbook_item.x, self.hbook_item.y, self.hbook_item.w, self.hbook_item.h)
    wgt_main.setStyleSheet(f'''background: {self.hbook_item.bg};
                            border-radius: {self.hbook_item.br}px;''')
    
    # lb_pic
    lb_pic = QLabel(wgt_main)
    lb_pic.setGeometry(self.hbook_item.pic_x, self.hbook_item.pic_y, self.hbook_item.pic_w, self.hbook_item.pic_h)
    lb_pic.setScaledContents(True)
    lb_pic.setCursor(QCursor(Qt.PointingHandCursor))
    # use a pic to download
    sszpthread = sszpThread(func=lambda: load_pic(lb_pic, download.book.cover))
    sszpthread.start()

    lb_pic.mousePressEvent = lambda eve: self.download_launcher_not_append(download.book)

    # te_title
    te_t = QTextEdit(wgt_main)
    te_t.setGeometry(self.hbook_item.t_x, self.hbook_item.t_y, self.hbook_item.t_w, self.hbook_item.t_h)
    te_t.setText(f'<a style="color: {color_title}; font-style: italic;">{download.book.title}</a>')
    te_t.setReadOnly(True)
    te_t.setFrameShape(QFrame.Shape.NoFrame)
    te_t.setFont(QFont(times_, 12))
    te_t.setCursor(QCursor(Qt.PointingHandCursor))
    te_t.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    # lb_press
    lb_p = QLabel(wgt_main)
    lb_p.setGeometry(self.hbook_item.p_x, self.hbook_item.p_y, self.hbook_item.p_w, self.hbook_item.p_h)
    lb_p.setText(download.book.press)
    lb_p.setFont(QFont(times_, 12))
    lb_p.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    # lb_author
    lb_a = QLabel(wgt_main)
    lb_a.setGeometry(self.hbook_item.a_x, self.hbook_item.a_y, self.hbook_item.a_w, self.hbook_item.a_h)
    lb_a.setText(download.book.author)
    lb_a.setFont(QFont(times_, 12))
    lb_a.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    lb_a.setStyleSheet(f'color: {color_author}; text-decoration: underline;')

    # lb_zlib
    lb_z = QLabel(wgt_main)
    lb_z.setGeometry(self.hbook_item.z_x, self.hbook_item.z_y, self.hbook_item.z_w, self.hbook_item.z_h)
    lb_z.setCursor(QCursor(Qt.PointingHandCursor))
    lb_z.setText(f'zlib: {download.book.url}')
    lb_z.setFont(QFont(times_, 11))
    # hover
    lb_z.enterEvent = lambda eve: lb_z.setStyleSheet(f'color: {color_title}')
    lb_z.leaveEvent = lambda eve: lb_z.setStyleSheet(f'color: {color_black}')
    # callback
    lb_z.mousePressEvent = lambda eve: open_url(download.book.url) # redownload
    
    # lb_l 
    lb_l = QLabel(wgt_main)
    lb_l.setGeometry(self.hbook_item.l_x, self.hbook_item.l_y, self.hbook_item.l_w, self.hbook_item.l_h)
    lb_l.setText(f'{download.book.language}')
    lb_l.setFont(QFont(times_, 11))

    # lb_year
    lb_y = QLabel(wgt_main)
    lb_y.setGeometry(self.hbook_item.y_x, self.hbook_item.y_y, self.hbook_item.y_w, self.hbook_item.y_h)
    lb_y.setText(f'{download.book.year}')
    lb_y.setFont(QFont(times_, 11))

    # lb_el
    lb_el = QLabel(wgt_main)
    lb_el.setGeometry(self.hbook_item.el_x, self.hbook_item.el_y, self.hbook_item.el_w, self.hbook_item.el_h)
    lb_el.setText(f'{download.book.extension}, {download.book.length}')
    lb_el.setFont(QFont(times_, 11))
    
    with QMutexLocker(self.mutex):
        self.gl_history_book.addWidget(wgt_main, gx, gy)

# use to append history search
# use history_search because of need to show the cover
def append_history_search(self, search: History_Search, gx: int, gy: int):
    # append to history search
    
    wgt_main = QWidget()
    wgt_main.setFixedWidth(self.search_item.w)
    wgt_main.setFixedHeight(self.search_item.h)
    wgt_main.setGeometry(self.search_item.x, self.search_item.y, self.search_item.w, self.search_item.h)
    wgt_main.setStyleSheet(f'''background: {self.search_item.bg};
                            border-radius: {self.search_item.br}px;''')
    
    # lb_pic
    lb_pic = QLabel(wgt_main)
    lb_pic.setGeometry(self.search_item.pic_x, self.search_item.pic_y, self.search_item.pic_w, self.search_item.pic_h)
    lb_pic.setScaledContents(True)
    lb_pic.setCursor(QCursor(Qt.PointingHandCursor))
    sszpthread = sszpThread(func=lambda: load_pic(lb_pic, search.cover))
    sszpthread.start()

    # relaunch
    lb_pic.mousePressEvent = lambda eve: self.search_launcher_not_append(search.search)

    # q
    lb_q = QLabel(wgt_main)
    lb_q.setGeometry(self.search_item.q_x, self.search_item.q_y, self.search_item.q_w, self.search_item.q_h)
    lb_q.setText(f'<a style="color: {color_q}; font-style: italic;">{search.search.q}</a>')
    lb_q.setFont(QFont(times_, 15))
    lb_q.setCursor(QCursor(Qt.PointingHandCursor))
    lb_q.setAlignment(Qt.AlignmentFlag.AlignHCenter) # alignment Horizontal Center

    # search type
    lb_st = QLabel(wgt_main)
    lb_st.setGeometry(self.search_item.st_x, self.search_item.st_y, self.search_item.st_w, self.search_item.st_h)

    lb_st.setText(f'{search.search.search_type} search')
    lb_st.setFont(QFont(times_, 12))
    
    # year
    lb_y = QLabel(wgt_main)
    lb_y.setGeometry(self.search_item.y_x, self.search_item.y_y, self.search_item.y_w, self.search_item.y_h)

    lb_y.setText(f'from {search.search.year_from} to {search.search.year_to}')
    lb_y.setFont(QFont(times_, 12))

    # comb_language
    comb_l = QComboBox(wgt_main)
    comb_l.setGeometry(self.search_item.l_x, self.search_item.l_y, self.search_item.l_w, self.search_item.l_h)
        # sim is StandardItemModel
    sim_l = QStandardItemModel()
    for lang in search.search.languages:
        sim_l.appendRow(QStandardItem(lang))
    comb_l.setModel(sim_l)
    comb_l.setFont(QFont(times_, 12))
    
    # book nums
    lb_bn = QLabel(wgt_main)
    lb_bn.setGeometry(self.search_item.bn_x, self.search_item.bn_y, self.search_item.bn_w, self.search_item.bn_h)

    lb_bn.setText(f'book nums: {search.search.book_nums}')
    lb_bn.setFont(QFont(times_, 12))

    # comb_extension
    comb_ex = QComboBox(wgt_main)
    comb_ex.setGeometry(self.search_item.ex_x, self.search_item.ex_y, self.search_item.ex_w, self.search_item.ex_h)
    sim_ex = QStandardItemModel()
    for ex in search.search.extensions:
        sim_ex.appendRow(QStandardItem(ex))
    comb_ex.setModel(sim_ex)
    comb_ex.setFont(QFont(times_, 12))

    # lb_t
    lb_t = QLabel(wgt_main)
    lb_t.setGeometry(self.search_item.t_x, self.search_item.t_y, self.search_item.t_w, self.search_item.t_h)
    
    lb_t.setText(f'time: {search.search.time.ymdhm()}')
    lb_t.setFont(QFont(times_, 12))

    # lb_em
    lb_em = QLabel(wgt_main)
    lb_em.setGeometry(self.search_item.em_x, self.search_item.em_y, self.search_item.em_w, self.search_item.em_h)

    lb_em.setText(f'<a>Exact: {search.search.exact_matching_bool()}</a>')
    lb_em.setFont(QFont(times_, 12))

    with QMutexLocker(self.mutex): 
        # add wgt_main to gridLayout
        self.gl_history_search.addWidget(wgt_main, gx, gy)

