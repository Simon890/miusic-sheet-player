import numpy as np
from figures.Rectangle import Rectangle
from figures.Figure import Figure
from figures.Circle import Circle
from figures.Triangle import Triangle
import os
import shutil
import cv2

class Generator:
    
    BBOX_WIDTH_MAX = 50
    BBOX_WIDTH_MIN = 10
    BBOX_HEIGHT_MAX = 50
    BBOX_HEIGHT_MIN = 10
    BATCH_SIZE=25
    
    __img = np.array([], dtype=np.int32)
    __figures : list[Figure] = []
    __images = []
    __dataset = []
    
    def generate_db(self, ds_size:int, test_size:int):
        self.__create_dirs()
        count = 1
        for i in range(ds_size + 1):
            print("Generating... ", i)
            #Random figure on image
            num_figs = np.random.randint(0, 5)
            #Random type of figures
            class_figs = np.random.randint(0, 3, size=num_figs)
            
            img = self.__gen_empty_img()
            for class_fig in class_figs:
                img = self.__draw_fig(class_fig, img)
            self.__images.append(img)
            self.__dataset.append((img.copy(), self.__figures.copy()))
            self.__figures = []
            
            if(len(self.__images) == self.BATCH_SIZE or (ds_size < self.BATCH_SIZE and len(self.__images) == ds_size)):
                dataset = self.__gen_x_y()
                self.__dataset = []
                self.__images = []
                split_idx = max(1, int(round(test_size * self.BATCH_SIZE)))
                rand_idx = np.random.permutation(len(dataset))
                for j in range(0, split_idx):
                    # print("Test", j)
                    row = dataset[j]
                    image = row[0]
                    bbox_str_arr = row[1]
                    cv2.imwrite(f"./dataset/test/{count}.png", image)
                    with open(f"./dataset/test/{count}.txt", "w") as file:
                        for bbox_str in bbox_str_arr:
                            file.write(bbox_str)
                        file.close()
                    count += 1
                for j in range(split_idx, len(dataset)):
                    # print("Train", j)
                    row = dataset[j]
                    image = row[0]
                    bbox_str_arr = row[1]
                    cv2.imwrite(f"./dataset/train/{count}.png", image)
                    with open(f"./dataset/train/{count}.txt", "w") as file:
                        for bbox_str in bbox_str_arr:
                            file.write(bbox_str)
                        file.close()
                    count += 1
                
    
    def __gen_x_y(self):
        images = []
        for row in self.__dataset:
            img = row[0]
            figures = row[1]
            figures_str = []
            for fig in figures:
                figures_str.append(fig.bbox.to_str() + "\n")
            images.append((img, figures_str))
        return images
    
    def __create_dirs(self):
        if not os.path.isdir("./dataset"):
            os.mkdir("./dataset")
        else:
            shutil.rmtree("./dataset/")
            os.mkdir("./dataset")
        
        os.mkdir("./dataset/train")
        os.mkdir("./dataset/test")
    
    def __draw_fig(self, class_fig: int, img: np.ndarray):
        if(class_fig == Rectangle.ID):
            return self.__draw_rect(img)
        if(class_fig == Circle.ID):
            return self.__draw_circle(img)
        if(class_fig == Triangle.ID):
            return self.__draw_triangle(img)
        return img
    
    def __draw_triangle(self, img: np.ndarray):
        triangle = None
        exit = False
        while not exit:
            pt1 = np.random.randint(0, 129, size=2, dtype=np.int32)
            pt2 = np.random.randint(0, 129, size=2, dtype=np.int32)
            pt3 = np.random.randint(0, 129, size=2, dtype=np.int32)
            triangle = Triangle(np.array([pt1, pt2, pt3], dtype=np.int32))
            
            collides = False
            for fig in self.__figures:
                if fig.collides(triangle):
                    collides = True
            
            if not collides:
                exit = True
                self.__figures.append(triangle)
        img_new = triangle.draw(img)
        return img_new
            
    
    def __draw_circle(self, img: np.ndarray):
        circle = None
        exit = False
        while not exit:
            pt1 = np.random.randint(0, 129, size=2, dtype=np.int32)
            radius = np.random.randint(self.BBOX_WIDTH_MIN // 2, self.BBOX_WIDTH_MAX // 2, dtype=np.int32)
            
            if(pt1[0] + radius > 128 or pt1[1] + radius > 128 or pt1[0] - radius < 0 or pt1[1] - radius < 0):
                continue
            
            circle = Circle(np.array([pt1], dtype=np.int32), radius)
            collides = False
            for fig in self.__figures:
                if fig.collides(circle):
                    collides = True
            if not collides:
                exit = True
                self.__figures.append(circle)
        img_new = circle.draw(img)
        return img_new

    
    def __draw_rect(self, img: np.ndarray):
        rect = None
        exit = False
        while not exit:
            pt1 = np.random.randint(0, 129, size=2, dtype=np.int32)
            pt2x = None
            pt2y = None
            
            #X axis
            if(pt1[0] + self.BBOX_WIDTH_MAX > 128):
                pt2x = np.random.randint(pt1[0] - self.BBOX_WIDTH_MAX, pt1[0] - self.BBOX_WIDTH_MIN)
            else:
                pt2x = np.random.randint(pt1[0] + self.BBOX_WIDTH_MIN, pt1[0] + self.BBOX_WIDTH_MAX)
            
            #Y axis
            if(pt1[1] + self.BBOX_HEIGHT_MAX > 128):
                pt2y = np.random.randint(pt1[1] - self.BBOX_HEIGHT_MAX, pt1[1] - self.BBOX_HEIGHT_MIN)
            else:
                pt2y = np.random.randint(pt1[1] + self.BBOX_HEIGHT_MIN, pt1[1] + self.BBOX_HEIGHT_MAX)
            
            pt2 = np.array([pt2x, pt2y], dtype=np.int32)
            coords = np.array([pt1, pt2], dtype=np.int32)
            rect = Rectangle(coords)
            collides = False
            for fig in self.__figures:
                if fig.collides(rect):
                    collides = True
            
            if not collides:
                exit = True
                self.__figures.append(rect)
        img_new = rect.draw(img)
        return img_new
    
    def __gen_empty_img(self):
        return np.ones(shape=(128, 128), dtype=np.int32) * 255