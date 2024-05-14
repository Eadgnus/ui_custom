import cv2
import os
import yaml

from PySide6.QtWidgets import QFileDialog


class Label_info:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Label_info, cls).__new__(cls, *args, **kwargs)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self.img_full_path = []
        self.labels = []  # 라벨 리스트
        self.labels2 = []  # 라벨 리스트
        self.labeled = {}  # 라벨 된 정보
        self.labeled2 = {}  # 라벨 된 정보
        self.rect_list = []
        self.rect_list2 = []
        self.labels_dict = {}
        self.labels_dict2 = {}
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

    def update_labels_dict(self):
        for idx, label in enumerate(self.labels):
            self.labels_dict[label] = idx

        for idx, label in enumerate(self.labels2):
            self.labels_dict2[label] = idx

    def save_datasets(self, save_datasets=0):
        self.update_labels_dict()
        output_path = QFileDialog.getExistingDirectory(None, "Select Folder")
        shuffle_idx = 0

        if not os.path.exists(os.path.join(output_path, "train/images")):
            os.makedirs(os.path.join(output_path, "train/images"), exist_ok=True)
            os.makedirs(os.path.join(output_path, "train/labels"), exist_ok=True)
            os.makedirs(os.path.join(output_path, "valid/images"), exist_ok=True)
            os.makedirs(os.path.join(output_path, "valid/labels"), exist_ok=True)
            os.makedirs(os.path.join(output_path, "test/images"), exist_ok=True)
            os.makedirs(os.path.join(output_path, "test/labels"), exist_ok=True)

            os.makedirs(os.path.join(output_path, "train/labels2"), exist_ok=True)
            os.makedirs(os.path.join(output_path, "valid/labels2"), exist_ok=True)
            os.makedirs(os.path.join(output_path, "test/labels2"), exist_ok=True)

        for (img_full_path, item), (_, item2) in zip(self.labeled.items(), self.labeled2.items()):
            img_name = img_full_path.split('\\')[-1].split(".jpg")[0].split("/")[-1]
            img = cv2.imread(img_full_path)
            mode = "train" if shuffle_idx < 7 else "valid" if shuffle_idx < 9 else "test"
            shuffle_idx = shuffle_idx + 1 if shuffle_idx < 10 else 0
            save_folder = os.path.join(output_path, mode)
            save_img_path = os.path.join(save_folder, "images", img_name)
            save_label_path = os.path.join(save_folder, "labels", img_name)
            cv2.imwrite(f"{save_img_path}.jpg", img)

            with open(f"{save_label_path}.txt", "w") as file:
                for _, value in item.items():
                    label, coorps = value
                    label = self.labels_dict[label]
                    file.write(f"{label}\t{coorps[0]}\t{coorps[1]}\t{coorps[2]}\t{coorps[3]}\n")

            yaml_text = f'''train: {output_path}/train/images
valid: {output_path}/valid/images
test: {output_path}/valid/images

nc: {len(self.labels)}
names: {self.labels}
'''
            with open(f"{output_path}/data.yaml", "w") as f:
                f.write(yaml_text)

            save_label_path2 = os.path.join(output_path, mode, "labels2")
            with open(f"{save_label_path2}/{img_name}.txt", "w") as file:
                for _, value in item2.items():
                    label, coorps = value
                    label = self.labels_dict2[label]
                    file.write(f"{label}\t{coorps[0]}\t{coorps[1]}\t{coorps[2]}\t{coorps[3]}\n")

            yaml_text2 = f'''train: {output_path}/train/images
valid: {output_path}/valid/images
test: {output_path}/valid/images

nc: {len(self.labels2)}
names: {self.labels2}
'''
            with open(f"{output_path}/data2.yaml", "w") as f:
                f.write(yaml_text2)

    def update_class(self):
        # 2번째의 데이터셋만 불러왔을 경우
        if self.labels == []:
            self.labels = self.labels2
            self.labels2 = []
        if self.labeled == {}:
            self.labeled = self.labeled2
            self.labeled2 = {}

    def update_labels(self):
        self.labels = set()  # labels를 세트로 정의
        for _, value in self.labeled.items():
            for _, value2 in value.items():
                label = value2[0]
                if label not in self.labels:
                    self.labels.add(label)
        self.labels = list(self.labels)

        self.labels2 = set()  # labels를 세트로 정의
        for _, value in self.labeled2.items():
            for _, value2 in value.items():
                label = value2[0]
                if label not in self.labels2:
                    self.labels2.add(label)
        self.labels2 = list(self.labels2)
