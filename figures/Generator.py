import numpy as np
from figures.Rectangle import Rectangle
from figures.Figure import Figure
from figures.Circle import Circle
from figures.Triangle import Triangle

class Generator:
    
    BBOX_WIDTH_MAX = 50
    BBOX_WIDTH_MIN = 10
    BBOX_HEIGHT_MAX = 50
    BBOX_HEIGHT_MIN = 10
    
    __img = np.array([], dtype=np.int32)
    __figures : list[Figure] = []
    __images = []
    
    def generate_db(self, size:int):
        for i in range(size + 1):
            #Random figure on image
            num_figs = np.random.randint(0, 5)
            #Random type of figures
            class_figs = np.random.randint(0, 3, size=num_figs)
            
            img = self.__gen_empty_img()
            for class_fig in class_figs:
                img = self.__draw_fig(class_fig, img)
                self.__images.append(img)
        return self.__images
    
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
            
            pt2x = None
            pt2y = None
            
            if(pt1[0] + self.BBOX_WIDTH_MAX > 128):
                pt2x = np.random.randint(pt1[0] - self.BBOX_WIDTH_MAX, pt1[0] - self.BBOX_WIDTH_MIN)
            else:
                pt2x = np.random.randint(pt1[0] + self.BBOX_WIDTH_MIN, pt1[0] + self.BBOX_WIDTH_MAX)
                
            if(pt1[1] + self.BBOX_HEIGHT_MAX > 128):
                pt2y = np.random.randint(pt1[1] - self.BBOX_HEIGHT_MAX, pt1[1] - self.BBOX_HEIGHT_MIN)
            else:
                pt2y = np.random.randint(pt1[1] + self.BBOX_HEIGHT_MIN, pt1[1] + self.BBOX_HEIGHT_MAX)
            
            pt3 = np.random.randint(0, 129, size=2, dtype=np.int32)
            pt2 = np.array([pt2x, pt2y])
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
            radius = np.random.randint(self.BBOX_WIDTH_MIN, self.BBOX_WIDTH_MAX // 2, dtype=np.int32)
            
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