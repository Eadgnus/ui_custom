import os
import sys
import cv2
from PySide6.QtWidgets import *
from Process.main_page_info import Main_page_info

main_info = Main_page_info()


def open_folder():
    folder_path = QFileDialog.getExistingDirectory()
    main_info.update_folder_path(folder_path)
    main_info.update_img_list()
    print(main_info.get_img_list())



