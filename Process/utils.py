import os
import sys
import cv2
from PySide6.QtWidgets import *
from Process.main_page_info import Main_page_info
from Process.label_info import Label_info
from PySide6.QtGui import *
from PySide6.QtCore import Qt
import pickle

output_dir = ""

main_info = Main_page_info()
label_info = Label_info()


def open_folder():
    global main_info, label_info
    #
    # folder_path = QFileDialog.getExistingDirectory()
    # main_info.update_folder_path(folder_path)
    # main_info.update_img_list()
    #
    # file_path = QFileDialog.getOpenFileName()
    # open_project(file_path)

    # 사용자에게 선택지를 제공하는 메시지 박스 생성
    msgBox = QMessageBox()
    msgBox.setText("원하는 작업을 선택하세요.")
    msgBox.addButton("폴더 열기", QMessageBox.AcceptRole)
    msgBox.addButton("파일 열기", QMessageBox.RejectRole)
    ret = msgBox.exec()

    if ret == 0:
        # 폴더 열기 로직
        folder_path = QFileDialog.getExistingDirectory(None, "Select Folder")
        if folder_path:  # 사용자가 폴더를 선택했다면
            main_info.update_folder_path(folder_path)
    elif ret == 1:
        # 파일 열기 로직
        file_path, _ = QFileDialog.getOpenFileName(None, "Select File")
        if file_path:  # 사용자가 파일을 선택했다면
            open_project(file_path)
            saved_folder_path = label_info.img_full_path[0].split("\\")[:-1][0]
            main_info.update_folder_path(saved_folder_path)

def tolist(str):
    # 주어진 문자열
    str_value = str

    # 대괄호 제거
    str_value = str_value.strip("[]")

    # 쉼표로 분리하여 리스트 생성
    str_list = str_value.split(", ")

    # 각 문자열 요소를 정수형으로 변환
    int_list = [int(item) for item in str_list]
    return int_list

def save_project():
    # 파일로부터 객체 역직렬화 및 불러오기
    folder_path = QFileDialog.getExistingDirectory()
    with open(f'{folder_path}/save.pkl', 'wb') as f:
        pickle.dump(label_info, f)
        print(f'{"*" * 20}Save{"*" * 20}')
        print(f"len_label_info.img_full_path: {len(label_info.img_full_path)}")
        if len(label_info.labeled) > 0:
            print(f"label_info.labels: {label_info.labels}")
            print(f"label_info.labeled: {label_info.labeled}")
            print(f"label_info.rect_list: {label_info.rect_list}")

        if len(label_info.labeled2) > 0:
            print(f"label_info.labels2: {label_info.labels2}")
            print(f"label_info.labeled2: {label_info.labeled2}")
        print(f'{"*" * 20}----{"*" * 20}')
        print("저장되었습니다.")

def open_project(file_path):
    global label_info
    # 파일로부터 객체 역직렬화 및 불러오기
    with open(file_path, 'rb') as f:
        label_info = pickle.load(f)
        label_info.update_class()
        label_info.update_labels()
        print(f'{"*" * 20}Utils{"*" * 20}')
        print(f"len_label_info.img_full_path: {len(label_info.img_full_path)}")
        print("")
        if len(label_info.labeled) > 0:
            print(f"label_info.labels: {label_info.labels}")
            print(f"label_info.labeled: {label_info.labeled}")
        else:
            print("저장된 데이터가 없습니다.")
        if len(label_info.labeled2) > 0:
            print("")
            print(f"label_info.labels2: {label_info.labels2}")
            print(f"label_info.labeled2: {label_info.labeled2}")
        print(f'{"*" * 20}----{"*" * 20}')

def next_button():
    pass

def past_button():
    pass

