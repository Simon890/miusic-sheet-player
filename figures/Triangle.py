import cv2
from figures.Figure import Figure
import numpy as np
from figures.BoundingBox import BoundingBox

class Triangle(Figure):
    ID=2
    
    def draw(self, img):
        pt1 = self._coords[0]
        pt2 = self._coords[1]
        pt3 = self._coords[2]
        pts = np.array([[pt1, pt2, pt3]], dtype=np.int32)
        img_new = cv2.polylines(img, pts, True, 0)
        return cv2.drawContours(img_new, pts, 0, 0, -1)
    
    def _build_bbox(self):
        pt1 = self._coords[0]
        pt2 = self._coords[1]
        pt3 = self._coords[2]
        all_x = np.array([pt1[0], pt2[0], pt3[0]])
        all_y = np.array([pt1[1], pt2[1], pt3[1]])
        min_x = np.min(all_x)
        min_y = np.min(all_y)
        bbox_pt1 = [min_x, min_y]
        bbox_pt2 = [np.max(all_x), min_y]
        bbox_pt3 = [np.max(all_x), np.max(all_y)]
        bbox_pt4 = [min_x, np.max(all_y)]
        return BoundingBox(bbox_pt1, bbox_pt2, bbox_pt3, bbox_pt4)