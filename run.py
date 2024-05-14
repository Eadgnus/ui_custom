from ui_main import Ui_MainWindow
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from Process.utils import *

r'''
C:\Users\sosoe\Desktop\UI_custom\run.py:75: DeprecationWarning: Function: 'QMouseEvent.pos() const' is marked as deprecated, please check the documentation for more information.
  self.end_point = self.labeling_image_view.mapToScene(event.pos()).toPoint()
  마우스 포지션 리턴받는 과정에서 생기는 삭제예정 경고문구 제거
'''
import warnings

# DeprecationWarning을 무시하도록 설정
warnings.filterwarnings("ignore", category=DeprecationWarning)


# ui_main의 메인 리사이즈 변경 1220, 789
class Main_program(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_program, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("SHLab")
        # STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.title_label.mouseMoveEvent = self.moveWindow

        # 이미지 관련
        self.img = None
        self.current_img_index = 0
        self.current_img_full_path = None
        self.installEventFilter(self)

        # 사이드바 하나 우선 숨김 처리
        self.Sidebar_1.setHidden(True)

        # 페이지 이동
        self.main_button_1.clicked.connect(self.swich_to_MainPage)
        self.main_button_2.clicked.connect(self.swich_to_MainPage)
        self.main_next_button.clicked.connect(self.swich_to_LabelingPage)
        self.main_next_button.clicked.connect(self.swich_to_LabelingPage)

        self.labeling_button_1.clicked.connect(self.swich_to_LabelingPage)
        self.labeling_button_2.clicked.connect(self.swich_to_LabelingPage)

        # main page
        self.main_file_button.clicked.connect(self.main_file_button_click)
        self.selection_model = None

        # label page
        self.pixmap_item = None
        self.current_rect = None
        self.label_add_button.clicked.connect(self.label_add_button_click)
        self.label_delete_button.clicked.connect(self.label_delete_button_click)
        self.labeling_next_button.clicked.connect(self.swich_to_next_image)
        self.labeling_past_button.clicked.connect(self.swich_to_past_image)
        # 클래스에 저장된 라벨 가져오기
        for base_label in label_info.labels:
            self.labeling_list_view.addItem(base_label)

        # 마우스 조작 함수 등록
        self.start_point, self.moving_point, self.end_point = None, None, None
        self.labeling_image_view.mousePressEvent = self.image_view_mousePressEvent
        self.labeling_image_view.mouseMoveEvent = self.image_view_mouseMoveEvent
        self.labeling_image_view.mouseReleaseEvent = self.image_view_mouseReleaseEvent
        # self.labeling_image_view.paintEvent = self.image_view_paint_Event

        # 저장 버튼
        self.save_button_2.clicked.connect(self.save_project)

    # MOVE WINDOW / MAXIMIZE / RESTORE
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPosition().toPoint()

    def image_view_mouseMoveEvent(self, event):
        if not self.start_point is None:
            self.moving_point = self.labeling_image_view.mapToScene(event.pos()).toPoint()
            if not self.img is None:
                if not self.current_rect is None:
                    self.img.removeItem(self.current_rect)
                rect = QRect(self.start_point, self.moving_point)
                self.current_rect = self.img.addRect(rect, QPen(Qt.black))

    def image_view_mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = self.labeling_image_view.mapToScene(event.pos()).toPoint()

    def image_view_mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = self.labeling_image_view.mapToScene(event.pos()).toPoint()
            self.draw_bbox()

            # 모든것 처리 이후 마우스 포인트 초기화
            self.start_point, self.end_point = None, None

    def draw_bbox(self):
        if not self.img is None:
            self.img.removeItem(self.current_rect)
            rect = QRect(self.start_point, self.end_point)
            self.fix_rect = self.img.addRect(rect, QPen(Qt.black))
            bbox = [self.start_point.x(), self.start_point.y(), self.end_point.x(), self.end_point.y()]
            current_label = "라벨을 입력 or 선택 해주세요." if self.labeling_list_view.currentItem() is None else self.labeling_list_view.currentItem().text()
            current_label2 = "라벨을 입력 or 선택 해주세요." if self.labeling_list_view_2.currentItem() is None else self.labeling_list_view_2.currentItem().text()

            # 라벨 목록 가져오기
            self.labels_list = [self.labeling_list_view.item(i).text() for i in range(self.labeling_list_view.count())]
            if self.labeling_list_view_2_check.isChecked():
                self.labels_list2 = [self.labeling_list_view_2.item(i).text() for i in
                                     range(self.labeling_list_view_2.count())]

            # 현재 라벨의 인덱스 찾기
            if current_label in self.labels_list:
                current_index = self.labels_list.index(current_label)
            else:
                current_index = 0  # 라벨이 리스트에 없으면 첫 번째 항목을 기본값으로 사용


            # 사용자에게 라벨을 선택하게 하는 팝업창 띄우기
            current_label, ok = QInputDialog.getItem(self, "Select Label", "Please select a label:", self.labels_list,
                                                     current_index, False)

            # 현재 라벨의 인덱스 찾기
            if self.labeling_list_view_2_check.isChecked():
                if current_label2 in self.labels_list2:
                    current_index2 = self.labels_list2.index(current_label2)
                else:
                    current_index2 = 0  # 라벨이 리스트에 없으면 첫 번째 항목을 기본값으로 사용
                current_label2, ok2 = QInputDialog.getItem(self, "Select Label", "Please select a label:", self.labels_list2,
                                                         current_index2, False)

            if ok and current_label:  # 사용자가 삼각단추를 눌렀을 때
                # 라벨 목록에서 현재 라벨 찾기
                matching_items = self.labeling_list_view.findItems(current_label, Qt.MatchExactly)

                # 만약 현재 라벨이 라벨 목록에 없다면, 새로운 항목으로 추가
                if not matching_items:
                    self.labeling_list_view.addItem(current_label)
                    # 업데이트
                    self.labels_list = [self.labeling_list_view.item(i).text() for i in
                                        range(self.labeling_list_view.count())]
                label_info.labels = self.labels_list
                if self.labeling_list_view_2_check.isChecked():
                    if ok2 and current_label2:  # 사용자가 삼각단추를 눌렀을 때
                        # 라벨 목록에서 현재 라벨 찾기
                        matching_items2 = self.labeling_list_view_2.findItems(current_label2, Qt.MatchExactly)

                        # 만약 현재 라벨이 라벨 목록에 없다면, 새로운 항목으로 추가
                        if not matching_items2:
                            self.labeling_list_view_2.addItem(current_label2)
                            # 업데이트
                            self.labels_list2 = [self.labeling_list_view_2.item(i).text() for i in
                                                 range(self.labeling_list_view_2.count())]
                        label_info.labels2 = self.labels_list2
                if ok and current_label:
                    if self.labeling_list_view_2_check.isChecked():
                        if ok2 and current_label2:
                            self.current_label_info(current_label, bbox, current_label2)
                    else:
                        self.current_label_info(current_label, bbox)

            else:  # 취소시 사각형 지우기
                self.img.removeItem(self.fix_rect)


    def current_label_info(self, current_label, bbox, current_label2=None, current_img_full_path=None):
        if current_img_full_path is None:
            current_img_full_path = self.current_img_full_path

        # 이미지 ID에 해당하는 라벨 정보가 없으면 새로운 항목을 생성
        image_idx = 0
        image_idx2 = 0

        # 'labeled' 키의 존재 여부를 확인하고, 없으면 초기화
        if current_img_full_path not in label_info.labeled:
            label_info.labeled[current_img_full_path] = {}

        # 'current_label2'가 None이 아닌 경우 'labeled2' 키의 존재 여부를 확인하고, 없으면 초기화
        if current_label2 is not None and current_img_full_path not in label_info.labeled2:
            label_info.labeled2[current_img_full_path] = {}

        # bbox의 고유 키 생성
        bbox_key = image_idx
        while label_info.labeled[current_img_full_path].get(bbox_key) is not None:
            bbox_key += 1  # 이미 존재하는 키를 건너뛰기 위해 인덱스 증가

        if current_label2 is not None:
            bbox_key2 = image_idx2
            while label_info.labeled2[current_img_full_path].get(bbox_key2) is not None:
                bbox_key2 += 1  # 이미 존재하는 키를 건너뛰기 위해 인덱스 증가

        # bbox 정보와 클래스명을 딕셔너리에 추가
        label_info.labeled[current_img_full_path][bbox_key] = [current_label, bbox]
        if current_label2 is not None:
            label_info.labeled2[current_img_full_path][bbox_key2] = [current_label2, bbox]
        self.update_labeled_list_view()
        self.update_labeled_data_list_view()

    def moveWindow(self, event):
        # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:  # 오른쪽 방향키가 눌렸는지 확인
            self.swich_to_next_image()
        elif event.key() == Qt.Key_Left:  # 왼쪽 방향키가 눌렸는지 확인
            self.swich_to_past_image()

    def label_add_button_click(self):
        text, ok = QInputDialog.getText(self, 'Input Label', '라벨을 입력하세요.')
        if ok and text:
            choice_msg = QMessageBox()
            choice_msg.setWindowTitle('리스트 선택')
            choice_msg.setText('라벨을 추가할 리스트를 선택하세요.')
            choice_msg.addButton('1번', QMessageBox.AcceptRole)
            choice_msg.addButton('2번', QMessageBox.RejectRole)
            ret = choice_msg.exec_()

            if ret == 0:
                # 리스트 1에 추가
                self.labeling_list_view.addItem(text)
            else:
                # 리스트 2에 추가
                if self.labeling_list_view_2_check.isChecked():
                    self.labeling_list_view_2.addItem(text)
                else:
                    choice_msg = QMessageBox()
                    choice_msg.setWindowTitle('리스트 선택')
                    choice_msg.setText('오른쪽 리스트 위 체크박스 체크 후 사용해 주세요.')
                    choice_msg.exec_()

    def label_delete_button_click(self):
        current_item_labeling = self.labeling_list_view.currentItem()
        current_item_labeling2 = self.labeling_list_view_2.currentItem()
        current_item_labeled = self.labeled_list_view.currentItem()
        current_item_labeled_data = self.labeled_data_list_view.currentItem()

        # labeling_list_view에서 아이템이 선택된 경우
        if current_item_labeling is not None:
            reply = QMessageBox.question(self, '항목 삭제 확인',
                                         f'선택한 라벨 {current_item_labeling.text()}을(를) 정말 삭제하시겠습니까?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                row = self.labeling_list_view.row(current_item_labeling)  # 현재 아이템의 인덱스를 찾음
                self.labeling_list_view.takeItem(row)  # 해당 인덱스의 아이템을 삭제
                label_info.labels.remove(current_item_labeling.text())

        elif current_item_labeling2 is not None:
            reply = QMessageBox.question(self, '항목 삭제 확인',
                                         f'선택한 라벨 {current_item_labeling2.text()}을(를) 정말 삭제하시겠습니까?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                row = self.labeling_list_view_2.row(current_item_labeling2)  # 현재 아이템의 인덱스를 찾음
                self.labeling_list_view_2.takeItem(row)  # 해당 인덱스의 아이템을 삭제
                label_info.labels2.remove(current_item_labeling2.text())

        # labeled_list_view에서 아이템이 선택된 경우
        elif current_item_labeled is not None:
            reply = QMessageBox.question(self, '항목 삭제 확인',
                                         f'선택한 bbox {current_item_labeled.text()}을(를) 정말 삭제하시겠습니까?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                row = self.labeled_list_view.row(current_item_labeled)  # 현재 아이템의 인덱스를 찾음
                self.labeled_list_view.takeItem(row)  # 해당 인덱스의 아이템을 삭제

                current_label = current_item_labeled.text().split("\t")[0]
                # rect_list 순회
                current_xywh = current_item_labeled.text().split("\t")[-1]
                # str -> lsit 변환
                current_xywh = tolist(current_xywh)

                # label_info.labeled2 딕셔너리에서도 제거
                # label_info.labeled와 label_info.labeled2 딕셔너리에서 제거
                self.remove_label_info(current_label, label_info.labeled, self.current_img_full_path)
                self.remove_label_info(current_label, label_info.labeled2, self.current_img_full_path)


        # labeled_data_list_view에서 아이템이 선택된 경우
        elif current_item_labeled_data is not None:
            reply = QMessageBox.question(self, '항목 삭제 확인',
                                         f'{current_item_labeled_data.text()}을(를) 정말 삭제하시겠습니까?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                row = self.labeled_data_list_view.row(current_item_labeled_data)  # 현재 아이템의 인덱스를 찾음
                self.labeled_data_list_view.takeItem(row)  # 해당 인덱스의 아이템을 삭제

                if label_info.labeled.get(current_item_labeled_data.text()) is not None:
                    del label_info.labeled[current_item_labeled_data.text()]
                if label_info.labeled2.get(current_item_labeled_data.text()) is not None:
                    del label_info.labeled2[current_item_labeled_data.text()]

        self.update_labeling_img(self.current_img_index)
        self.update_labeled_data_list_view()
        self.clear_selections()

    def remove_label_info(self, label, label_dict, current_img_path):
        """
        지정된 이미지 경로에서 특정 라벨 정보를 제거합니다.
        """
        if label_dict.get(current_img_path) is not None:
            for key, info in label_dict[current_img_path].copy().items():
                if info[0] == label:
                    del label_dict[current_img_path][key]
                    break  # 일치하는 첫 항목을 찾으면 반복 중단


    def main_file_button_click(self):
        open_folder()
        # list view에 이미지 넣어줘야함

        self.main_folder_input.insert(main_info.get_folder_path())
        img_list = main_info.get_full_path()

        # 모든 이미지 label_info에 img_path 추가
        label_info.img_full_path = img_list

        # img_list의 각 항목을 모델에 추가
        for img_path in img_list:
            self.main_image_list_view.addItem(img_path)

        # 이미지 리스트 선택 될때마다
        self.selection_model = self.main_image_list_view.selectionModel()
        self.selection_model.selectionChanged.connect(self.on_selection_changed)

        # 라벨 이미지도 넣어주기
        self.current_img_full_path = img_list[0]

        # 라벨된 부분 업데이트
        self.update_labeled_list_view()
        self.update_labeled_data_list_view()
        # self.labeling_img = self.show_img(img_list[0])
        # self.labeling_image_view.setScene(self.labeling_img)
        # self.labeling_image_view.show()

    # 이미지 리스트에서 선택이 변경될 때 호출될 함수를 정의합니다.
    def on_selection_changed(self, selected, deselected):
        # 선택된 항목들의 인덱스를 얻습니다.
        indexes = selected.indexes()

        # 선택된 각 항목에 대한 텍스트를 출력합니다.
        for index in indexes:
            # 선택된 곳의 요소
            select_path = index.data(Qt.DisplayRole)

        # 이미지 뷰어창에 이미지 넣기
        self.img = self.show_img(select_path)
        self.main_image_view.setScene(self.img)
        self.main_image_view.fitInView(self.pixmap_item, Qt.KeepAspectRatio)
        self.main_image_view.show()

        # 라벨링 창에도 넣어주기
        self.change_current_labeling_image()
        self.update_labeled_list_view()
        self.update_labeled_data_list_view()

    # 페이지 이동 함수
    def swich_to_MainPage(self):
        self.page_container.setCurrentIndex(0)

    def swich_to_LabelingPage(self):
        self.page_container.setCurrentIndex(1)
        self.labeling_button_2.setChecked(True)

    def change_current_labeling_image(self, current_img=None):
        self.labeled_list_view.clear()
        if current_img is None:
            current_img = self.img
        self.labeling_image_view.setScene(current_img)
        self.labeling_image_view.fitInView(self.pixmap_item, Qt.KeepAspectRatio)
        self.labeling_image_view.show()

        # 첫 번째 라벨 정보 처리
        if label_info.labeled.get(self.current_img_full_path) is not None:
            current_info = label_info.labeled[self.current_img_full_path]
            for key, info in current_info.items():
                self.draw_label_rect(info)

        # 두 번째 라벨 정보 처리
        if label_info.labeled2.get(self.current_img_full_path) is not None:
            current_info2 = label_info.labeled2[self.current_img_full_path]
            for key, info in current_info2.items():
                self.draw_label_rect(info)

        # labeled data 불러오기
        self.update_label_list_view()
        self.update_labeled_list_view()
        self.update_labeled_data_list_view()

    def draw_label_rect(self, info):
        label, coords = info[0], info[1]
        start_x, start_y, end_x, end_y = coords
        width = end_x - start_x
        height = end_y - start_y
        rect = QRect(start_x, start_y, width, height)
        self.img.addRect(rect, QPen(Qt.black))
    def update_labeled_list_view(self):
        try:
            self.labeled_list_view.clear()
            current_info = label_info.labeled.get(self.current_img_full_path, {})

            current_info2 = label_info.labeled2.get(self.current_img_full_path, {})

            # labeled와 labeled2에서 고유 키(예: bbox ID)의 합집합을 구합니다.
            all_keys = set(current_info.keys()) | set(current_info2.keys())

            for key in all_keys:
                info = current_info.get(key)
                info2 = current_info2.get(key)

                # 두 딕셔너리 중 하나에만 정보가 있을 수 있으므로, 그 경우를 처리합니다.
                if info:
                    label, coords = info[0], info[1]
                    self.labeled_list_view.addItem(f"{label}\t{coords}")
                if info2:
                    label, coords = info2[0], info2[1]
                    self.labeled_list_view.addItem(f"{label}\t{coords}")
        except:
            pass

    def update_label_list_view(self):
        self.labeling_list_view.clear()
        self.labeling_list_view_2.clear()

        self.labeling_list_view.addItems(label_info.labels)
        self.labeling_list_view_2.addItems(label_info.labels2)

    def update_labeled_data_list_view(self):
        self.labeled_data_list_view.clear()

        # Empty labels to be removed
        empty_labels = [key for key, info in label_info.labeled.items() if not info]
        empty_labels2 = [key for key, info in label_info.labeled2.items() if not info]

        # Remove empty labels
        for key in empty_labels:
            del label_info.labeled[key]

        for key in empty_labels2:
            del label_info.labeled2[key]

        # Add non-empty labels to the list view
        non_empty_labels = set(list(label_info.labeled.keys()) + list(label_info.labeled2.keys()))
        for key in non_empty_labels:
            self.labeled_data_list_view.addItem(key)

    # 라벨링 사진 넘기기
    def update_labeling_img(self, current_img_index):
        max_len = len(main_info.get_full_path()) - 1  # index와 len의 특성 차이
        if max_len == -1:
            return
        if max_len < current_img_index:
            self.current_img_index = 0
        elif current_img_index < 0:
            self.current_img_index = max_len

        self.current_img_full_path = main_info.get_full_path()[self.current_img_index]
        self.img = self.show_img(self.current_img_full_path)
        self.change_current_labeling_image()

    def show_img(self, img_path):
        # 이미지 로드
        pixmap = QPixmap(img_path)

        # QGraphicsPixmapItem 생성
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.pixmap_item = pixmap_item

        # QGraphicsScene 생성 및 설정
        scene = QGraphicsScene()
        scene.setSceneRect(pixmap.rect())
        scene.addItem(pixmap_item)

        return scene

    def swich_to_next_image(self):
        self.current_img_index = self.current_img_index + 1
        self.update_labeling_img(self.current_img_index)

    def swich_to_past_image(self):
        self.current_img_index = self.current_img_index - 1
        self.update_labeling_img(self.current_img_index)

    def save_project(self):
        msgBox = QMessageBox()
        msgBox.setText("원하는 작업을 선택하세요.")
        msgBox.addButton("작업 현황 저장하기", QMessageBox.AcceptRole)
        msgBox.addButton("이미지와 데이터셋으로 저장하기", QMessageBox.RejectRole)
        ret = msgBox.exec()

        if ret == 0:
            save_project()
        else:
            save_project()
            label_info.save_datasets()

    def clear_selections(self):
        # 모든 선택 해제
        self.labeling_list_view.clearSelection()
        self.labeling_list_view_2.clearSelection()
        self.labeled_list_view.clearSelection()
        self.labeled_data_list_view.clearSelection()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_program()
    window.show()

    sys.exit(app.exec())
