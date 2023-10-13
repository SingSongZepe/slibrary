# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slibrary.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1121, 721)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setStyleSheet(u"#wgt_main {\n"
"	background: #ffffff;\n"
"}\n"
"\n"
"#lb_home_selected {\n"
"	background: #4ce2ff;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#wgt_main_home {\n"
"	background: #ffffff;\n"
"}\n"
"#wgt_main_search {\n"
"	background: #ffffff;\n"
"}\n"
"#wgt_main_setting {\n"
"	background: #ffffff;\n"
"}\n"
"#wgt_main_history {\n"
"	background: #ffffff;\n"
"}\n"
"#wgt_main_recommend {\n"
"	background: #ffffff;\n"
"}\n"
"\n"
"/*\n"
"#lb_by {\n"
"	color: white;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #f7b500, stop:0.5153 #b620e0, stop:1 #4ce2ff);\n"
"	border-radius: 10px;\n"
"}\n"
"#lb_by:pressed {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4ce2ff, stop:0.5153 #b620e0, stop:1 #f7b500);\n"
"}\n"
"*/\n"
"#tb_logue {\n"
"	color: #333333;\n"
"}\n"
"\n"
"/* search */\n"
"#pb_search {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #00b4db, stop:1 #0083b0);\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    bo"
                        "rder-radius: 4px;\n"
"}\n"
"#pb_search:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #00d8ff, stop:1 #00a6c4);\n"
"}\n"
"#pb_search:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #006c8a, stop:1 #004f64);\n"
"}\n"
"#le_search {\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	border-radius: 4px;\n"
"	background: #f0f0f0;\n"
"}\n"
"\n"
"/* history */\n"
"#lb_history_temp {\n"
"	color: #ffffff;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #f7b500, stop:0.5153 #b620e0, stop:1 #4ce2ff);\n"
"}\n"
"#lb_history_search {\n"
"	background: #e0e0e0;\n"
"}\n"
"#lb_history_search:hover {\n"
"	background: #f0f0f0;\n"
"}\n"
"#lb_history_book:hover {\n"
"	background: #f0f0f0;\n"
"}\n"
"#lb_history_clear:hover {\n"
"	background: #f0f0f0;\n"
"}\n"
"\n"
"/* recommmend */\n"
"#lb_recommend_temp {\n"
"	color: #ffffff;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #f7b500, stop:0.5153 #b620e0, stop:1 #4ce2f"
                        "f);\n"
"}\n"
"\n"
"/* settings */\n"
"#wgt_for_sa_settings {\n"
"	background: #ffffff;\n"
"}\n"
"#lb_settings {\n"
"	color: #ffffff;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #f7b500, stop:0.5153 #b620e0, stop:1 #4ce2ff);\n"
"}\n"
"#wgt_settings_deco {\n"
"	background: #e0e0e0;\n"
"}\n"
"#lb_setting_search {\n"
"	background: #f0f0f0;\n"
"	padding-left: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.wgt_tab = QWidget(self.centralwidget)
        self.wgt_tab.setObjectName(u"wgt_tab")
        self.wgt_tab.setGeometry(QRect(0, 50, 41, 671))
        self.line_2 = QFrame(self.wgt_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 115, 30, 3))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line = QFrame(self.wgt_tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 65, 30, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.wgt_tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 165, 30, 3))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.wgt_tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 215, 30, 3))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.wgt_home = QWidget(self.wgt_tab)
        self.wgt_home.setObjectName(u"wgt_home")
        self.wgt_home.setGeometry(QRect(0, 20, 30, 40))
        self.lb_wgt_home = QLabel(self.wgt_home)
        self.lb_wgt_home.setObjectName(u"lb_wgt_home")
        self.lb_wgt_home.setGeometry(QRect(2, 0, 26, 26))
        self.lb_wgt_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_home_selected = QLabel(self.wgt_home)
        self.lb_home_selected.setObjectName(u"lb_home_selected")
        self.lb_home_selected.setGeometry(QRect(5, 30, 20, 4))
        self.wgt_search = QWidget(self.wgt_tab)
        self.wgt_search.setObjectName(u"wgt_search")
        self.wgt_search.setGeometry(QRect(0, 70, 30, 40))
        self.lb_wgt_search = QLabel(self.wgt_search)
        self.lb_wgt_search.setObjectName(u"lb_wgt_search")
        self.lb_wgt_search.setGeometry(QRect(2, 0, 26, 26))
        self.lb_wgt_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_search_selected = QLabel(self.wgt_search)
        self.lb_search_selected.setObjectName(u"lb_search_selected")
        self.lb_search_selected.setGeometry(QRect(5, 30, 20, 4))
        self.wgt_recommend = QWidget(self.wgt_tab)
        self.wgt_recommend.setObjectName(u"wgt_recommend")
        self.wgt_recommend.setGeometry(QRect(0, 120, 30, 40))
        self.lb_wgt_recommend = QLabel(self.wgt_recommend)
        self.lb_wgt_recommend.setObjectName(u"lb_wgt_recommend")
        self.lb_wgt_recommend.setGeometry(QRect(2, 0, 26, 26))
        self.lb_wgt_recommend.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_recommend_selected = QLabel(self.wgt_recommend)
        self.lb_recommend_selected.setObjectName(u"lb_recommend_selected")
        self.lb_recommend_selected.setGeometry(QRect(5, 30, 20, 4))
        self.wgt_history = QWidget(self.wgt_tab)
        self.wgt_history.setObjectName(u"wgt_history")
        self.wgt_history.setGeometry(QRect(0, 170, 30, 40))
        self.lb_wgt_history = QLabel(self.wgt_history)
        self.lb_wgt_history.setObjectName(u"lb_wgt_history")
        self.lb_wgt_history.setGeometry(QRect(2, 0, 26, 26))
        self.lb_wgt_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_history_selected = QLabel(self.wgt_history)
        self.lb_history_selected.setObjectName(u"lb_history_selected")
        self.lb_history_selected.setGeometry(QRect(5, 30, 20, 4))
        self.wgt_setting = QWidget(self.wgt_tab)
        self.wgt_setting.setObjectName(u"wgt_setting")
        self.wgt_setting.setGeometry(QRect(0, 220, 30, 40))
        self.lb_wgt_setting = QLabel(self.wgt_setting)
        self.lb_wgt_setting.setObjectName(u"lb_wgt_setting")
        self.lb_wgt_setting.setGeometry(QRect(2, 0, 26, 26))
        self.lb_wgt_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_setting_selected = QLabel(self.wgt_setting)
        self.lb_setting_selected.setObjectName(u"lb_setting_selected")
        self.lb_setting_selected.setGeometry(QRect(5, 30, 20, 4))
        self.wgt_head = QWidget(self.centralwidget)
        self.wgt_head.setObjectName(u"wgt_head")
        self.wgt_head.setGeometry(QRect(0, 0, 71, 71))
        self.lb_head = QLabel(self.wgt_head)
        self.lb_head.setObjectName(u"lb_head")
        self.lb_head.setGeometry(QRect(0, 0, 71, 71))
        self.wgt_bar = QWidget(self.centralwidget)
        self.wgt_bar.setObjectName(u"wgt_bar")
        self.wgt_bar.setGeometry(QRect(50, 0, 1071, 21))
        self.lb_quit = QLabel(self.wgt_bar)
        self.lb_quit.setObjectName(u"lb_quit")
        self.lb_quit.setGeometry(QRect(1035, 0, 20, 20))
        self.lb_quit.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_minimize = QLabel(self.wgt_bar)
        self.lb_minimize.setObjectName(u"lb_minimize")
        self.lb_minimize.setGeometry(QRect(985, 0, 20, 20))
        self.lb_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_full = QLabel(self.wgt_bar)
        self.lb_full.setObjectName(u"lb_full")
        self.lb_full.setGeometry(QRect(935, 0, 20, 20))
        self.lb_full.setCursor(QCursor(Qt.PointingHandCursor))
        self.line_5 = QFrame(self.wgt_bar)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(970, 0, 3, 31))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.wgt_bar)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(1020, 0, 3, 31))
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.wgt_main = QWidget(self.centralwidget)
        self.wgt_main.setObjectName(u"wgt_main")
        self.wgt_main.setGeometry(QRect(30, 20, 1091, 701))
        self.wgt_main_home = QWidget(self.wgt_main)
        self.wgt_main_home.setObjectName(u"wgt_main_home")
        self.wgt_main_home.setGeometry(QRect(0, 0, 1091, 701))
        self.verticalLayoutWidget = QWidget(self.wgt_main_home)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 30, 1091, 80))
        self.vl_slibrary = QVBoxLayout(self.verticalLayoutWidget)
        self.vl_slibrary.setObjectName(u"vl_slibrary")
        self.vl_slibrary.setContentsMargins(0, 0, 0, 0)
        self.lb_slibrary = QLabel(self.verticalLayoutWidget)
        self.lb_slibrary.setObjectName(u"lb_slibrary")
        self.lb_slibrary.setPixmap(QPixmap(u"../res/img/slibrary.png"))
        self.lb_slibrary.setScaledContents(False)
        self.lb_slibrary.setAlignment(Qt.AlignCenter)

        self.vl_slibrary.addWidget(self.lb_slibrary)

        self.verticalLayoutWidget_2 = QWidget(self.wgt_main_home)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 530, 1071, 121))
        self.vl_by = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vl_by.setObjectName(u"vl_by")
        self.vl_by.setContentsMargins(0, 0, 0, 0)
        self.lb_by = QLabel(self.verticalLayoutWidget_2)
        self.lb_by.setObjectName(u"lb_by")
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(25)
        self.lb_by.setFont(font1)
        self.lb_by.setAlignment(Qt.AlignCenter)

        self.vl_by.addWidget(self.lb_by)

        self.lb_thanks = QLabel(self.verticalLayoutWidget_2)
        self.lb_thanks.setObjectName(u"lb_thanks")
        font2 = QFont()
        font2.setFamilies([u"Agency FB"])
        font2.setPointSize(12)
        self.lb_thanks.setFont(font2)
        self.lb_thanks.setTextFormat(Qt.AutoText)
        self.lb_thanks.setAlignment(Qt.AlignCenter)

        self.vl_by.addWidget(self.lb_thanks)

        self.verticalLayoutWidget_3 = QWidget(self.wgt_main_home)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 180, 1091, 141))
        self.vl_logue = QVBoxLayout(self.verticalLayoutWidget_3)
        self.vl_logue.setObjectName(u"vl_logue")
        self.vl_logue.setContentsMargins(0, 0, 0, 0)
        self.tb_logue = QTextBrowser(self.verticalLayoutWidget_3)
        self.tb_logue.setObjectName(u"tb_logue")
        self.tb_logue.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"ScriptS"])
        font3.setPointSize(16)
        self.tb_logue.setFont(font3)
        self.tb_logue.setLayoutDirection(Qt.LeftToRight)
        self.tb_logue.setFrameShape(QFrame.NoFrame)

        self.vl_logue.addWidget(self.tb_logue)

        self.wgt_main_search = QWidget(self.wgt_main)
        self.wgt_main_search.setObjectName(u"wgt_main_search")
        self.wgt_main_search.setGeometry(QRect(0, 0, 1091, 701))
        self.wgt_result = QWidget(self.wgt_main_search)
        self.wgt_result.setObjectName(u"wgt_result")
        self.wgt_result.setGeometry(QRect(30, 220, 1031, 481))
        self.line_7 = QFrame(self.wgt_result)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(0, 0, 3, 481))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy)
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.wgt_result)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(0, 0, 1031, 3))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_9 = QFrame(self.wgt_result)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(1030, 0, 3, 481))
        sizePolicy.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy)
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget_6 = QWidget(self.wgt_main_search)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(100, 60, 881, 81))
        self.vl_wgt_search_ctan = QVBoxLayout(self.verticalLayoutWidget_6)
        self.vl_wgt_search_ctan.setSpacing(0)
        self.vl_wgt_search_ctan.setObjectName(u"vl_wgt_search_ctan")
        self.vl_wgt_search_ctan.setSizeConstraint(QLayout.SetMaximumSize)
        self.vl_wgt_search_ctan.setContentsMargins(0, 0, 0, 0)
        self.wgt_le_search_ctan = QWidget(self.verticalLayoutWidget_6)
        self.wgt_le_search_ctan.setObjectName(u"wgt_le_search_ctan")
        self.le_search = QLineEdit(self.wgt_le_search_ctan)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setGeometry(QRect(50, 10, 721, 60))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(14)
        self.le_search.setFont(font4)
        self.le_search.setAutoFillBackground(False)
        self.le_search.setMaxLength(49)
        self.le_search.setFrame(True)
        self.pb_search = QPushButton(self.wgt_le_search_ctan)
        self.pb_search.setObjectName(u"pb_search")
        self.pb_search.setGeometry(QRect(740, 10, 91, 60))
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(12)
        self.pb_search.setFont(font5)
        self.pb_search.setCursor(QCursor(Qt.PointingHandCursor))

        self.vl_wgt_search_ctan.addWidget(self.wgt_le_search_ctan)

        self.line_12 = QFrame(self.wgt_main_search)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(0, 180, 1090, 3))
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.wgt_main_history = QWidget(self.wgt_main)
        self.wgt_main_history.setObjectName(u"wgt_main_history")
        self.wgt_main_history.setGeometry(QRect(0, 0, 1091, 701))
        self.lb_history_book = QLabel(self.wgt_main_history)
        self.lb_history_book.setObjectName(u"lb_history_book")
        self.lb_history_book.setGeometry(QRect(60, 110, 51, 51))
        self.lb_history_book.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_history_book.setStyleSheet(u"")
        self.lb_history_book.setFrameShape(QFrame.Box)
        self.lb_history_book.setFrameShadow(QFrame.Sunken)
        self.lb_history_book.setScaledContents(True)
        self.lb_history_search = QLabel(self.wgt_main_history)
        self.lb_history_search.setObjectName(u"lb_history_search")
        self.lb_history_search.setGeometry(QRect(60, 60, 51, 51))
        self.lb_history_search.setFrameShape(QFrame.Box)
        self.lb_history_search.setFrameShadow(QFrame.Sunken)
        self.lb_history_temp = QLabel(self.wgt_main_history)
        self.lb_history_temp.setObjectName(u"lb_history_temp")
        self.lb_history_temp.setGeometry(QRect(110, 60, 871, 51))
        font6 = QFont()
        font6.setFamilies([u"Agency FB"])
        font6.setPointSize(20)
        font6.setBold(False)
        self.lb_history_temp.setFont(font6)
        self.lb_history_temp.setAlignment(Qt.AlignCenter)
        self.wgt_history_book = QWidget(self.wgt_main_history)
        self.wgt_history_book.setObjectName(u"wgt_history_book")
        self.wgt_history_book.setGeometry(QRect(110, 110, 871, 591))
        self.wgt_history_book.setStyleSheet(u"")
        self.wgt_history_search = QWidget(self.wgt_main_history)
        self.wgt_history_search.setObjectName(u"wgt_history_search")
        self.wgt_history_search.setGeometry(QRect(110, 110, 871, 591))
        self.wgt_history_search.setStyleSheet(u"")
        self.lb_history_clear = QLabel(self.wgt_main_history)
        self.lb_history_clear.setObjectName(u"lb_history_clear")
        self.lb_history_clear.setGeometry(QRect(60, 160, 51, 51))
        self.lb_history_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.lb_history_clear.setStyleSheet(u"")
        self.lb_history_clear.setFrameShape(QFrame.Box)
        self.lb_history_clear.setFrameShadow(QFrame.Sunken)
        self.lb_history_clear.setScaledContents(True)
        self.wgt_history_book.raise_()
        self.wgt_history_search.raise_()
        self.lb_history_book.raise_()
        self.lb_history_search.raise_()
        self.lb_history_temp.raise_()
        self.lb_history_clear.raise_()
        self.wgt_main_recommend = QWidget(self.wgt_main)
        self.wgt_main_recommend.setObjectName(u"wgt_main_recommend")
        self.wgt_main_recommend.setGeometry(QRect(0, 0, 1091, 701))
        self.lb_recommend_cg = QLabel(self.wgt_main_recommend)
        self.lb_recommend_cg.setObjectName(u"lb_recommend_cg")
        self.lb_recommend_cg.setGeometry(QRect(30, 60, 51, 51))
        self.lb_recommend_cg.setFrameShape(QFrame.Box)
        self.lb_recommend_cg.setFrameShadow(QFrame.Sunken)
        self.lb_recommend_cg.setPixmap(QPixmap(u"../res/img/change.png"))
        self.lb_recommend_cg.setScaledContents(True)
        self.lb_recommend_temp = QLabel(self.wgt_main_recommend)
        self.lb_recommend_temp.setObjectName(u"lb_recommend_temp")
        self.lb_recommend_temp.setGeometry(QRect(80, 60, 931, 51))
        font7 = QFont()
        font7.setFamilies([u"Agency FB"])
        font7.setPointSize(20)
        self.lb_recommend_temp.setFont(font7)
        self.lb_recommend_temp.setAlignment(Qt.AlignCenter)
        self.wgt_recommend_book = QWidget(self.wgt_main_recommend)
        self.wgt_recommend_book.setObjectName(u"wgt_recommend_book")
        self.wgt_recommend_book.setGeometry(QRect(30, 110, 1031, 591))
        self.line_10 = QFrame(self.wgt_recommend_book)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(0, 0, 3, 591))
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.line_11 = QFrame(self.wgt_recommend_book)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(1030, 0, 3, 591))
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.lb_recommend_cgn = QLabel(self.wgt_main_recommend)
        self.lb_recommend_cgn.setObjectName(u"lb_recommend_cgn")
        self.lb_recommend_cgn.setGeometry(QRect(1010, 60, 51, 51))
        self.lb_recommend_cgn.setFrameShape(QFrame.Box)
        self.lb_recommend_cgn.setFrameShadow(QFrame.Sunken)
        self.lb_recommend_cgn.setPixmap(QPixmap(u"../res/img/change.png"))
        self.lb_recommend_cgn.setScaledContents(True)
        self.wgt_main_setting = QWidget(self.wgt_main)
        self.wgt_main_setting.setObjectName(u"wgt_main_setting")
        self.wgt_main_setting.setGeometry(QRect(0, 0, 1091, 701))
        self.wgt_main_setting_inner = QWidget(self.wgt_main_setting)
        self.wgt_main_setting_inner.setObjectName(u"wgt_main_setting_inner")
        self.wgt_main_setting_inner.setGeometry(QRect(30, 100, 1031, 601))
        self.sa_settings = QScrollArea(self.wgt_main_setting_inner)
        self.sa_settings.setObjectName(u"sa_settings")
        self.sa_settings.setGeometry(QRect(0, 0, 1031, 601))
        self.sa_settings.setWidgetResizable(True)
        self.sawc_settings = QWidget()
        self.sawc_settings.setObjectName(u"sawc_settings")
        self.sawc_settings.setGeometry(QRect(0, 0, 1029, 599))
        self.wgt_for_sa_settings = QWidget(self.sawc_settings)
        self.wgt_for_sa_settings.setObjectName(u"wgt_for_sa_settings")
        self.wgt_for_sa_settings.setGeometry(QRect(0, 0, 1031, 601))
        self.wgt_settings_deco = QWidget(self.wgt_for_sa_settings)
        self.wgt_settings_deco.setObjectName(u"wgt_settings_deco")
        self.wgt_settings_deco.setGeometry(QRect(40, 0, 10, 51))
        self.lb_setting_search = QLabel(self.wgt_for_sa_settings)
        self.lb_setting_search.setObjectName(u"lb_setting_search")
        self.lb_setting_search.setGeometry(QRect(50, 0, 251, 51))
        self.lb_setting_search.setFont(font4)
        self.wgt_optional = QWidget(self.wgt_for_sa_settings)
        self.wgt_optional.setObjectName(u"wgt_optional")
        self.wgt_optional.setGeometry(QRect(40, 50, 261, 551))
        self.comb_search_type = QComboBox(self.wgt_optional)
        self.comb_search_type.addItem("")
        self.comb_search_type.addItem("")
        self.comb_search_type.setObjectName(u"comb_search_type")
        self.comb_search_type.setGeometry(QRect(20, 20, 111, 31))
        self.comb_search_type.setMaxVisibleItems(2)
        self.comb_search_type.setMaxCount(2)
        self.comb_search_type.setDuplicatesEnabled(True)
        self.cb_from_year = QCheckBox(self.wgt_optional)
        self.cb_from_year.setObjectName(u"cb_from_year")
        self.cb_from_year.setGeometry(QRect(20, 60, 111, 31))
        self.cb_extensions = QCheckBox(self.wgt_optional)
        self.cb_extensions.setObjectName(u"cb_extensions")
        self.cb_extensions.setGeometry(QRect(20, 150, 111, 31))
        self.cb_book_nums = QCheckBox(self.wgt_optional)
        self.cb_book_nums.setObjectName(u"cb_book_nums")
        self.cb_book_nums.setGeometry(QRect(20, 210, 111, 31))
        self.cb_to_year = QCheckBox(self.wgt_optional)
        self.cb_to_year.setObjectName(u"cb_to_year")
        self.cb_to_year.setGeometry(QRect(20, 90, 111, 31))
        self.cb_languages = QCheckBox(self.wgt_optional)
        self.cb_languages.setObjectName(u"cb_languages")
        self.cb_languages.setGeometry(QRect(20, 120, 111, 31))
        self.cb_exact_matching = QCheckBox(self.wgt_optional)
        self.cb_exact_matching.setObjectName(u"cb_exact_matching")
        self.cb_exact_matching.setGeometry(QRect(20, 180, 141, 31))
        self.sa_settings.setWidget(self.sawc_settings)
        self.lb_settings = QLabel(self.wgt_main_setting)
        self.lb_settings.setObjectName(u"lb_settings")
        self.lb_settings.setGeometry(QRect(30, 50, 1031, 51))
        self.lb_settings.setFont(font7)
        self.lb_settings.setAlignment(Qt.AlignCenter)
        self.wgt_main_search.raise_()
        self.wgt_main_setting.raise_()
        self.wgt_main_history.raise_()
        self.wgt_main_recommend.raise_()
        self.wgt_main_home.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.wgt_tab.raise_()
        self.wgt_bar.raise_()
        self.wgt_main.raise_()
        self.wgt_head.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_wgt_home.setText("")
        self.lb_home_selected.setText("")
        self.lb_wgt_search.setText("")
        self.lb_search_selected.setText("")
        self.lb_wgt_recommend.setText("")
        self.lb_recommend_selected.setText("")
        self.lb_wgt_history.setText("")
        self.lb_history_selected.setText("")
        self.lb_wgt_setting.setText("")
        self.lb_setting_selected.setText("")
        self.lb_head.setText("")
        self.lb_quit.setText("")
        self.lb_minimize.setText("")
        self.lb_full.setText("")
        self.lb_slibrary.setText("")
        self.lb_by.setText(QCoreApplication.translate("MainWindow", u"By SingSongZepe", None))
        self.lb_thanks.setText(QCoreApplication.translate("MainWindow", u"Also Thanks for Pei Yufan for Providing Cookies", None))
        self.tb_logue.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'ScriptS'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333333;\">Hello World</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333333;\">version 2</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#333333;\">Book downloader</span></p></body></html>", None))
        self.le_search.setInputMask("")
        self.le_search.setText("")
        self.le_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Book", None))
        self.pb_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lb_history_book.setText("")
        self.lb_history_search.setText("")
        self.lb_history_temp.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lb_history_clear.setText("")
        self.lb_recommend_cg.setText("")
        self.lb_recommend_temp.setText(QCoreApplication.translate("MainWindow", u"Recommend", None))
        self.lb_recommend_cgn.setText("")
        self.lb_setting_search.setText(QCoreApplication.translate("MainWindow", u"Search Setting", None))
        self.comb_search_type.setItemText(0, QCoreApplication.translate("MainWindow", u"general", None))
        self.comb_search_type.setItemText(1, QCoreApplication.translate("MainWindow", u"fulltext", None))

        self.cb_from_year.setText(QCoreApplication.translate("MainWindow", u"From Year", None))
        self.cb_extensions.setText(QCoreApplication.translate("MainWindow", u"Extensions", None))
        self.cb_book_nums.setText(QCoreApplication.translate("MainWindow", u"Book Nums", None))
        self.cb_to_year.setText(QCoreApplication.translate("MainWindow", u"To Year", None))
        self.cb_languages.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.cb_exact_matching.setText(QCoreApplication.translate("MainWindow", u"Exact Matching", None))
        self.lb_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

