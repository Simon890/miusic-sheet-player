import cv2
from figures.Figure import Figure
import numpy as np
from figures.BoundingBox import BoundingBox

class Rectangle(Figure):
    ID=1
    
    def draw(self, img : np.ndarray):
        pt1 = self._coords[0]
        pt2 = self._coords[1]
        return cv2.rectangle(img, pt1, pt2, 0, -1)
    
    def _build_bbox(self):
        pt1 = self._coords[0]
        pt3 = self._coords[1]
        pt2 = [pt3[0], pt1[1]]
        pt4 = [pt1[0], pt3[1]]
        return BoundingBox(pt1, pt2, pt3, pt4)