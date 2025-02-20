from figures.Figure import Figure
import numpy as np
import cv2

class Circle(Figure):
    _radius : int
    
    def __init__(self, coords, radius):
        super().__init__(coords)
        self._radius = radius
    
    def draw(self, img: np.ndarray):
        center = self._coords[0]
        return cv2.circle(img, center, self._radius, 0, -1)
    
    def get_bounding_box(self):
        center = self._coords[0]
        center_x = center[0]
        center_y = center[1]
        pt1 = [center_x - self._radius, center_y - self._radius]
        pt2 = [center_x + self._radius, center_y - self._radius]
        pt3 = [center_x + self._radius, center_y + self._radius]
        pt4 = [center_x - self._radius, center_y + self._radius]
        return np.array([pt1, pt2, pt3, pt4])