import cv2
import glob
import numpy as np

class Dataset:
    
    def __init__(self):
        pass
    
    def load(self, mode="train"):
        imgs_train_path = glob.glob(f"./dataset/{mode}/*.png")
        images = []
        classes = []
        for img_path in imgs_train_path[0:]:
            img_data = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            imgs_label_path = img_path.replace(".png", ".txt")
            class_list = [0, 0, 0]
            test_class = []
            with open(imgs_label_path, "r") as file:
                imgs_label_str = file.readlines()
                for imgs_label_row in imgs_label_str:
                    imgs_label_float = list(map(lambda x: float(x), imgs_label_row.split(" ")))
                    figure_class = int(imgs_label_float[0])
                    class_list[figure_class - 1] += 1
                    test_class.append(figure_class)
                file.close()
            classes.append(class_list)
            images.append(img_data)
        return np.array(images), np.array(classes)