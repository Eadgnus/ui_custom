import cv2
import os

class Label_info:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Label_info, cls).__new__(cls, *args, **kwargs)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self.img_full_path = []
        self.labels = []    # 라벨 리스트
        self.labeled = {}   # 라벨 된 정보
        self.rect_list = []
        '''
        labeled에 들어갈 정보
        id: full path,
        class: 라벨,
        bbox: bounding box,
        img: 이미지 객체,
        labeled: {"id": {"bbox1": [class, bbox]},
        "id": {"bbox2": [class, bbox]},
        ...
        }
        '''

    def save_datasets(self):
        for img_full_path, value in self.labeled.items():
            img_name = img_full_path.split('\\')[-1].split(".jpg")[0].split("/")[-1]
            img = cv2.imread(img_full_path)
            cv2.imwrite()
