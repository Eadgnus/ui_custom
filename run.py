from ui_main import Ui_MainWindow
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from Process.utils import open_folder, open_project, save_project
from Process.utils import main_info, label_info


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

            # 라벨 목록 가져오기
            self.labels_list = [self.labeling_list_view.item(i).text() for i in range(self.labeling_list_view.count())]

            # 현재 라벨의 인덱스 찾기
            if current_label in self.labels_list:
                current_index = self.labels_list.index(current_label)
            else:
                current_index = 0  # 라벨이 리스트에 없으면 첫 번째 항목을 기본값으로 사용

            # 사용자에게 라벨을 선택하게 하는 팝업창 띄우기
            current_label, ok = QInputDialog.getItem(self, "Select Label", "Please select a label:", self.labels_list,
                                                     current_index, False)

            if ok and current_label:  # 사용자가 삼각단추를 눌렀을 때
                # 라벨 목록에서 현재 라벨 찾기
                matching_items = self.labeling_list_view.findItems(current_label, Qt.MatchExactly)

                # 만약 현재 라벨이 라벨 목록에 없다면, 새로운 항목으로 추가
                if not matching_items:
                    self.labeling_list_view.addItem(current_label)
                    # 업데이트
                    self.labels_list = [self.labeling_list_view.item(i).text() for i in
                                        range(self.labeling_list_view.count())]
                self.current_label_info(current_label, bbox)
                label_info.labels = self.labels_list
            else:  # 취소시 사각형 지우기
                self.img.removeItem(self.fix_rect)

    def current_label_info(self, current_label, bbox, current_img_full_path = None):
        if current_img_full_path is None:
            current_img_full_path = self.current_img_full_path
        print("이미지 주소 144번줄: ", current_img_full_path)# None
        # 이미지 ID에 해당하는 라벨 정보가 없으면 새로운 항목을 생성
        image_idx = 0
        try:
            label_info.labeled[current_img_full_path]
        except:
            label_info.labeled[current_img_full_path] = {}

        # bbox의 고유 키 생성 (예: bbox1, bbox2, ...)
        try:
            while label_info.labeled[current_img_full_path][image_idx]:
                image_idx += 1
        except:
            bbox_key = image_idx

        # bbox 정보와 클래스명을 딕셔너리에 추가
        label_info.labeled[current_img_full_path][bbox_key] = [current_label, bbox]
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
        self.labeling_list_view.addItem(text)

    def label_delete_button_click(self):
        current_item_labeling = self.labeling_list_view.currentItem()
        current_item_labeled = self.labeled_list_view.currentItem()
        current_item_labeled_data = self.labeled_data_list_view.currentItem()

        # labeling_list_view에서 아이템이 선택된 경우
        if current_item_labeling is not None:
            row = self.labeling_list_view.row(current_item_labeling)  # 현재 아이템의 인덱스를 찾음
            self.labeling_list_view.takeItem(row)  # 해당 인덱스의 아이템을 삭제

        # labeled_list_view에서 아이템이 선택된 경우
        elif current_item_labeled is not None:
            row = self.labeled_list_view.row(current_item_labeled)  # 현재 아이템의 인덱스를 찾음
            self.labeled_list_view.takeItem(row)  # 해당 인덱스의 아이템을 삭제
            # rect_list 순회
            current_xywh = current_item_labeled.text().split("\t")[-1]
            # str -> lsit 변환
            current_xywh = tolist(current_xywh)

            # label_info.labeled 딕셔너리에서도 제거
            for key, info in label_info.labeled[self.current_img_full_path].copy().items():
                if info[1] == current_xywh:
                    del label_info.labeled[self.current_img_full_path][key]
                    self.update_labeling_img(self.current_img_index)
                    self.update_labeled_data_list_view()
                    break  # 일치하는 첫 항목을 찾으면 반복 중단

        # labeled_data_list_view에서 아이템이 선택된 경우
        elif current_item_labeled_data is not None:
            row = self.labeled_data_list_view.row(current_item_labeled_data)  # 현재 아이템의 인덱스를 찾음
            self.labeled_data_list_view.takeItem(row)  # 해당 인덱스의 아이템을 삭제
            del label_info.labeled[current_item_labeled_data.text()]
            print(label_info.labeled)

    def main_file_button_click(self):
        open_folder()
        # list view에 이미지 넣어줘야함

        self.main_folder_input.insert(main_info.get_folder_path())
        img_list = main_info.get_full_path()

        # 모든 이미지 label_info에 img_path 추가
        label_info.img_full_path = img_list

        print("run 226: ", label_info.labeled)

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

        try:
            # 불러와서 처리
            current_info = label_info.labeled[self.current_img_full_path]
            for key, info in current_info.items():
                label, coords = info[0], info[1]
                # 시작점의 x, y 좌표
                start_x = coords[0]
                start_y = coords[1]

                # 종점의 x, y 좌표
                end_x = coords[2]
                end_y = coords[3]

                # 너비와 높이 계산
                width = end_x - start_x
                height = end_y - start_y

                # QRect 객체 생성
                rect = QRect(start_x, start_y, width, height)
                self.img.addRect(rect, QPen(Qt.black))

            # labeled data 불러오기
            self.update_labeled_list_view()
            self.update_labeled_data_list_view()
        except Exception as e:
            pass

    def update_labeled_list_view(self):
        print(f"run 310 - update labeled list view: {label_info.labeled}")
        try:
            self.labeled_list_view.clear()
            current_info = label_info.labeled[self.current_img_full_path]
            print(f"run 313 - update labeled list view: {current_info}")
            for key, info in current_info.items():
                label, coords = info[0], info[1]
                # labeled data 불러오기
                self.labeled_list_view.addItem(f"{label}\t{coords}")
        except:
            pass
    def update_labeled_data_list_view(self):
        try:
            self.labeled_data_list_view.clear()
            for key, info in label_info.labeled.items():
                print("run 319 - update_labeled_data_list_view:", label_info.labeled)
                if info == {}:
                    del label_info.labeled[key]
                self.labeled_data_list_view.addItem(key)
        except:
            pass
    # 라벨링 사진 넘기기
    def update_labeling_img(self, current_img_index):
        max_len = len(main_info.get_full_path())-1  # index와 len의 특성 차이
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
        save_project()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_program()
    window.show()

    sys.exit(app.exec())
