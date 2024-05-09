from ui_main import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtGui import *
from Process.main_page_process import *

class Main_program(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_program, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("SHLab")

        # 사이드바 하나 우선 숨김 처리
        self.Sidebar_2.setHidden(True)

        # 페이지 이동
        self.main_button_1.clicked.connect(self.swich_to_MainPage)
        self.main_button_2.clicked.connect(self.swich_to_MainPage)
        self.main_next_button.clicked.connect(self.swich_to_LabelingPage)
        self.main_next_button.clicked.connect(self.swich_to_LabelingPage)

        self.labeling_button_1.clicked.connect(self.swich_to_LabelingPage)
        self.labeling_button_2.clicked.connect(self.swich_to_LabelingPage)

        # main page
        self.main_file_button.clicked.connect(self.main_file_button_click)


    def main_file_button_click(self):
        open_folder()
        # list view에 이미지 넣어줘야함

        self.main_folder_input.insert(main_info.get_folder_path())
        img_list = main_info.get_full_path()

        model = QStandardItemModel()
        for f in img_list:
            model.appendRow(QStandardItem(f))
        self.main_image_list_view.setModel(model)
        
    # 페이지 이동 함수
    def swich_to_MainPage(self):
        self.page_container.setCurrentIndex(0)

    def swich_to_LabelingPage(self):
        self.page_container.setCurrentIndex(1)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_program()
    window.show()

    sys.exit(app.exec())
