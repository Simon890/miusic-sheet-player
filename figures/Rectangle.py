import cv2
from figures.Figure import Figure
import numpy as np

class Rectangle(Figure):
    
    def draw(self, img : np.ndarray):
        pt1 = self._coords[0]
        pt2 = self._coords[1]
        return cv2.rectangle(img, pt1, pt2, 0, -1)
    
    def get_bounding_box(self):
        pt1 = self._coords[0]
        pt2 = self._coords[1]
        pt3 = [pt2[0], pt1[1]]
        pt4 = [pt1[0], pt2[1]]
        return np.array([pt1, pt3, pt2, pt4])