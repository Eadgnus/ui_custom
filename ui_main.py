# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainSAErum.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QGraphicsView, QGridLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1220, 789)
        MainWindow.setMinimumSize(QSize(1220, 789))
        MainWindow.setMaximumSize(QSize(1311, 789))
        MainWindow.setStyleSheet(u"margin:0;\n"
"padding: 0;\n"
"text-align:center;\n"
"background-color: #E37171;")
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Sidebar_2 = QWidget(self.centralwidget)
        self.Sidebar_2.setObjectName(u"Sidebar_2")
        self.Sidebar_2.setMinimumSize(QSize(119, 720))
        self.Sidebar_2.setMaximumSize(QSize(119, 16777215))
        self.Sidebar_2.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: #FFFFFF;\n"
"	color: rgb(254, 147, 140);\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"* {\n"
"	background-color: rgb(254, 147, 140);\n"
"	color: white;\n"
"}")
        self.logo_2 = QPushButton(self.Sidebar_2)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(-1, 0, 120, 50))
        self.logo_2.setMaximumSize(QSize(120, 16777215))
        self.logo_2.setStyleSheet(u"border:None;\n"
"background-color:None;")
        icon = QIcon()
        icon.addFile(u":/logo_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_2.setIcon(icon)
        self.logo_2.setIconSize(QSize(120, 50))
        self.logo_2.setCheckable(True)
        self.logo_2.setChecked(True)
        self.logo_2.setAutoExclusive(False)
        self.layoutWidget = QWidget(self.Sidebar_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 100, 121, 132))
        self.button_layout_2 = QVBoxLayout(self.layoutWidget)
        self.button_layout_2.setSpacing(20)
        self.button_layout_2.setObjectName(u"button_layout_2")
        self.button_layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.button_layout_2.setContentsMargins(10, 0, 0, 0)
        self.main_button_2 = QPushButton(self.layoutWidget)
        self.main_button_2.setObjectName(u"main_button_2")
        self.main_button_2.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        self.main_button_2.setFont(font)
        self.main_button_2.setStyleSheet(u"border: None;\n"
"text-align:left;\n"
"padding-left:5px;\n"
"\n"
"border-top-left-radius: 7px;\n"
"border-bottom-left-radius: 7px;")
        icon1 = QIcon()
        icon1.addFile(u":/main_2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/main_1.png", QSize(), QIcon.Normal, QIcon.On)
        self.main_button_2.setIcon(icon1)
        self.main_button_2.setIconSize(QSize(20, 20))
        self.main_button_2.setCheckable(True)
        self.main_button_2.setChecked(True)
        self.main_button_2.setAutoExclusive(True)

        self.button_layout_2.addWidget(self.main_button_2)

        self.labeling_button_2 = QPushButton(self.layoutWidget)
        self.labeling_button_2.setObjectName(u"labeling_button_2")
        self.labeling_button_2.setMinimumSize(QSize(0, 30))
        self.labeling_button_2.setFont(font)
        self.labeling_button_2.setStyleSheet(u"border: None;\n"
"text-align:left;\n"
"border-top-left-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"padding-left:5px;")
        icon2 = QIcon()
        icon2.addFile(u":/pencil_2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/pencil_1.png", QSize(), QIcon.Normal, QIcon.On)
        self.labeling_button_2.setIcon(icon2)
        self.labeling_button_2.setIconSize(QSize(20, 20))
        self.labeling_button_2.setCheckable(True)
        self.labeling_button_2.setAutoExclusive(True)

        self.button_layout_2.addWidget(self.labeling_button_2)

        self.save_button_2 = QPushButton(self.layoutWidget)
        self.save_button_2.setObjectName(u"save_button_2")
        self.save_button_2.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.save_button_2.setFont(font1)
        self.save_button_2.setStyleSheet(u"border: None;\n"
"text-align:left;\n"
"border-top-left-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"padding-left:5px;")
        icon3 = QIcon()
        icon3.addFile(u":/save_2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/save_1.png", QSize(), QIcon.Normal, QIcon.On)
        self.save_button_2.setIcon(icon3)
        self.save_button_2.setIconSize(QSize(20, 20))
        self.save_button_2.setCheckable(True)
        self.save_button_2.setAutoExclusive(True)

        self.button_layout_2.addWidget(self.save_button_2)


        self.gridLayout.addWidget(self.Sidebar_2, 0, 1, 1, 1)

        self.page_layout = QVBoxLayout()
        self.page_layout.setSpacing(0)
        self.page_layout.setObjectName(u"page_layout")
        self.title_label = QWidget(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QSize(1080, 49))
        self.title_label.setMaximumSize(QSize(1080, 49))
        self.title_label.setStyleSheet(u"background-color: rgb(234, 210, 172);\n"
"")
        self.close_button = QPushButton(self.title_label)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(1030, 2, 45, 45))
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        self.close_button.setMaximumSize(QSize(45, 45))
        self.close_button.setTabletTracking(False)
        self.close_button.setStyleSheet(u"border:None;\n"
"margin-right: 0px;")
        icon4 = QIcon()
        icon4.addFile(u":/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon4)
        self.close_button.setIconSize(QSize(45, 45))
        self.close_button.setCheckable(True)

        self.page_layout.addWidget(self.title_label)

        self.page_container = QStackedWidget(self.centralwidget)
        self.page_container.setObjectName(u"page_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page_container.sizePolicy().hasHeightForWidth())
        self.page_container.setSizePolicy(sizePolicy1)
        self.page_container.setMinimumSize(QSize(1080, 720))
        self.page_container.setMaximumSize(QSize(1080, 720))
        self.page_container.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.MainPage.setStyleSheet(u"")
        self.main_folder_input = QLineEdit(self.MainPage)
        self.main_folder_input.setObjectName(u"main_folder_input")
        self.main_folder_input.setGeometry(QRect(50, 10, 431, 21))
        self.main_next_button = QCommandLinkButton(self.MainPage)
        self.main_next_button.setObjectName(u"main_next_button")
        self.main_next_button.setGeometry(QRect(1015, 650, 41, 51))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.main_next_button.setFont(font2)
        self.main_next_button.setStyleSheet(u"text-align:center;")
        icon5 = QIcon()
        icon5.addFile(u":/next_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.main_next_button.setIcon(icon5)
        self.main_next_button.setIconSize(QSize(30, 30))
        self.main_next_button.setCheckable(False)
        self.main_image_list_view = QListWidget(self.MainPage)
        self.main_image_list_view.setObjectName(u"main_image_list_view")
        self.main_image_list_view.setGeometry(QRect(50, 50, 471, 591))
        self.main_image_list_view.setMaximumSize(QSize(471, 591))
        self.main_image_view = QGraphicsView(self.MainPage)
        self.main_image_view.setObjectName(u"main_image_view")
        self.main_image_view.setGeometry(QRect(550, 50, 511, 591))
        self.main_image_view.setMaximumSize(QSize(511, 591))
        self.main_file_button = QPushButton(self.MainPage)
        self.main_file_button.setObjectName(u"main_file_button")
        self.main_file_button.setGeometry(QRect(490, 10, 31, 23))
        icon6 = QIcon()
        icon6.addFile(u":/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.main_file_button.setIcon(icon6)
        self.page_container.addWidget(self.MainPage)
        self.LabelingPage = QWidget()
        self.LabelingPage.setObjectName(u"LabelingPage")
        self.LabelingPage.setMaximumSize(QSize(1080, 720))
        self.labeling_list_view = QListWidget(self.LabelingPage)
        self.labeling_list_view.setObjectName(u"labeling_list_view")
        self.labeling_list_view.setGeometry(QRect(5, 40, 121, 111))
        self.labeling_image_view = QGraphicsView(self.LabelingPage)
        self.labeling_image_view.setObjectName(u"labeling_image_view")
        self.labeling_image_view.setGeometry(QRect(250, 0, 831, 661))
        self.labeling_next_button = QCommandLinkButton(self.LabelingPage)
        self.labeling_next_button.setObjectName(u"labeling_next_button")
        self.labeling_next_button.setGeometry(QRect(1030, 670, 31, 41))
        self.labeling_next_button.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/next.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/next_2.png", QSize(), QIcon.Normal, QIcon.On)
        icon7.addFile(u":/next_2.png", QSize(), QIcon.Active, QIcon.On)
        icon7.addFile(u":/next_2.png", QSize(), QIcon.Selected, QIcon.On)
        self.labeling_next_button.setIcon(icon7)
        self.labeling_next_button.setCheckable(False)
        self.labeling_next_button.setAutoRepeat(False)
        self.labeling_next_button.setDefault(False)
        self.labeling_past_button = QCommandLinkButton(self.LabelingPage)
        self.labeling_past_button.setObjectName(u"labeling_past_button")
        self.labeling_past_button.setGeometry(QRect(260, 670, 31, 41))
        icon8 = QIcon()
        icon8.addFile(u":/past.png", QSize(), QIcon.Normal, QIcon.Off)
        self.labeling_past_button.setIcon(icon8)
        self.label = QLabel(self.LabelingPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(98, 4, 81, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(18)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(254, 147, 140);")
        self.label_add_button = QPushButton(self.LabelingPage)
        self.label_add_button.setObjectName(u"label_add_button")
        self.label_add_button.setGeometry(QRect(30, 680, 75, 24))
        self.label_add_button.setFont(font2)
        self.label_add_button.setStyleSheet(u"* {\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	color: black;\n"
"	background-color: white;\n"
"}\n"
"QPushButton:clicked{\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	background-color: black;\n"
"}")
        self.label_delete_button = QPushButton(self.LabelingPage)
        self.label_delete_button.setObjectName(u"label_delete_button")
        self.label_delete_button.setGeometry(QRect(140, 680, 75, 24))
        self.label_delete_button.setFont(font2)
        self.label_delete_button.setStyleSheet(u"* {border: 1px solid red;\n"
"border-radius: 5px;\n"
"color: red;\n"
"background-color: white;\n"
"}\n"
"QPushButton:clicked{\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	background-color: red;\n"
"}")
        self.labeled_data_list_view = QListWidget(self.LabelingPage)
        self.labeled_data_list_view.setObjectName(u"labeled_data_list_view")
        self.labeled_data_list_view.setGeometry(QRect(10, 390, 231, 271))
        self.label_2 = QLabel(self.LabelingPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 350, 141, 31))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(254, 147, 140);")
        self.labeled_list_view = QListWidget(self.LabelingPage)
        self.labeled_list_view.setObjectName(u"labeled_list_view")
        self.labeled_list_view.setGeometry(QRect(10, 200, 231, 141))
        self.label_3 = QLabel(self.LabelingPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(87, 160, 81, 31))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(254, 147, 140);")
        self.labeling_list_view_2 = QListWidget(self.LabelingPage)
        self.labeling_list_view_2.setObjectName(u"labeling_list_view_2")
        self.labeling_list_view_2.setGeometry(QRect(125, 40, 121, 111))
        self.labeling_list_view_2_check = QRadioButton(self.LabelingPage)
        self.labeling_list_view_2_check.setObjectName(u"labeling_list_view_2_check")
        self.labeling_list_view_2_check.setGeometry(QRect(230, 10, 16, 21))
        self.labeling_list_view_2_check.setChecked(True)
        self.page_container.addWidget(self.LabelingPage)

        self.page_layout.addWidget(self.page_container)


        self.gridLayout.addLayout(self.page_layout, 0, 2, 1, 1)

        self.Sidebar_1 = QWidget(self.centralwidget)
        self.Sidebar_1.setObjectName(u"Sidebar_1")
        self.Sidebar_1.setMinimumSize(QSize(80, 720))
        self.Sidebar_1.setMaximumSize(QSize(80, 16777215))
        self.Sidebar_1.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: #FFFFFF;\n"
"	color: rgb(254, 147, 140);\n"
"}\n"
"\n"
"* {\n"
"	background-color: rgb(254, 147, 140);\n"
"	color: white;\n"
"}")
        self.logo_1 = QPushButton(self.Sidebar_1)
        self.logo_1.setObjectName(u"logo_1")
        self.logo_1.setEnabled(True)
        self.logo_1.setGeometry(QRect(15, -1, 49, 49))
        self.logo_1.setMaximumSize(QSize(49, 49))
        self.logo_1.setMouseTracking(False)
        self.logo_1.setStyleSheet(u"border: None;")
        icon9 = QIcon()
        icon9.addFile(u":/logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_1.setIcon(icon9)
        self.logo_1.setIconSize(QSize(120, 50))
        self.logo_1.setCheckable(True)
        self.logo_1.setAutoExclusive(False)
        self.logo_1.setAutoDefault(False)
        self.logo_1.setFlat(False)
        self.layoutWidget_2 = QWidget(self.Sidebar_1)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(15, 100, 51, 132))
        self.button_layout_1 = QVBoxLayout(self.layoutWidget_2)
        self.button_layout_1.setSpacing(20)
        self.button_layout_1.setObjectName(u"button_layout_1")
        self.button_layout_1.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.button_layout_1.setContentsMargins(0, 0, 0, 0)
        self.main_button_1 = QPushButton(self.layoutWidget_2)
        self.main_button_1.setObjectName(u"main_button_1")
        self.main_button_1.setMinimumSize(QSize(0, 30))
        self.main_button_1.setMaximumSize(QSize(49, 16777215))
        self.main_button_1.setStyleSheet(u"border: None;\n"
"border-radius: 10px;")
        self.main_button_1.setIcon(icon1)
        self.main_button_1.setIconSize(QSize(20, 20))
        self.main_button_1.setCheckable(True)
        self.main_button_1.setAutoExclusive(True)

        self.button_layout_1.addWidget(self.main_button_1)

        self.labeling_button_1 = QPushButton(self.layoutWidget_2)
        self.labeling_button_1.setObjectName(u"labeling_button_1")
        self.labeling_button_1.setMinimumSize(QSize(0, 30))
        self.labeling_button_1.setMaximumSize(QSize(49, 16777215))
        self.labeling_button_1.setStyleSheet(u"border: None;\n"
"border-radius: 10px;")
        self.labeling_button_1.setIcon(icon2)
        self.labeling_button_1.setIconSize(QSize(20, 20))
        self.labeling_button_1.setCheckable(True)
        self.labeling_button_1.setAutoExclusive(True)

        self.button_layout_1.addWidget(self.labeling_button_1)

        self.save_button_1 = QPushButton(self.layoutWidget_2)
        self.save_button_1.setObjectName(u"save_button_1")
        self.save_button_1.setMinimumSize(QSize(0, 30))
        self.save_button_1.setMaximumSize(QSize(49, 16777215))
        self.save_button_1.setStyleSheet(u"border: None;\n"
"border-radius: 10px;")
        self.save_button_1.setIcon(icon3)
        self.save_button_1.setIconSize(QSize(20, 20))
        self.save_button_1.setCheckable(True)
        self.save_button_1.setAutoExclusive(True)

        self.button_layout_1.addWidget(self.save_button_1)


        self.gridLayout.addWidget(self.Sidebar_1, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close_button.clicked.connect(MainWindow.close)
        self.logo_2.toggled.connect(self.Sidebar_2.setHidden)
        self.main_next_button.toggled.connect(self.labeling_button_2.setChecked)
        self.main_next_button.toggled.connect(self.labeling_button_1.setChecked)
        self.logo_2.toggled.connect(self.Sidebar_1.setVisible)
        self.save_button_2.toggled.connect(self.save_button_1.setChecked)
        self.labeling_button_1.toggled.connect(self.labeling_button_2.setChecked)
        self.logo_1.toggled.connect(self.Sidebar_1.setHidden)
        self.main_button_2.toggled.connect(self.main_button_1.setChecked)
        self.labeling_button_2.toggled.connect(self.labeling_button_1.setChecked)
        self.logo_1.toggled.connect(self.Sidebar_2.setVisible)
        self.main_button_1.toggled.connect(self.main_button_2.setChecked)
        self.save_button_1.toggled.connect(self.save_button_2.setChecked)
        self.main_button_1.toggled.connect(self.main_button_2.setChecked)

        self.page_container.setCurrentIndex(0)
        self.logo_1.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_2.setText("")
        self.main_button_2.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.labeling_button_2.setText(QCoreApplication.translate("MainWindow", u"Labeling", None))
        self.save_button_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.close_button.setText("")
        self.main_folder_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ud3f4\ub354\ub97c \uc120\ud0dd\ud574\uc8fc\uc138\uc694", None))
        self.main_next_button.setText("")
        self.main_file_button.setText("")
        self.labeling_next_button.setText("")
        self.labeling_past_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.label_add_button.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00", None))
        self.label_delete_button.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Labeled Data", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Labeled", None))
        self.labeling_list_view_2_check.setText("")
        self.logo_1.setText("")
        self.main_button_1.setText("")
        self.labeling_button_1.setText("")
        self.save_button_1.setText("")
    # retranslateUi

