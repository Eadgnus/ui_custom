import os

class Main_page_info:
    def __init__(self):
        self.folder_path = ""
        self.img_list = []

    def update_folder_path(self, path):
        self.folder_path = path

    def get_folder_path(self):
        return self.folder_path

    def update_img_list(self):
        self.img_list = os.listdir(self.folder_path)

    def get_img_list(self):
        return self.img_list

    def get_full_path(self):
        img_full_path_list = []
        for img in self.img_list:
            img_full_path_list.append(os.path.join(self.folder_path, img))
        return img_full_path_list