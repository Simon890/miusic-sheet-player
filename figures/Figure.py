import abc
import cv2
import numpy as np
from typing_extensions import Self
from figures.BoundingBox import BoundingBox

class Figure(abc.ABC):
    
    _coords: np.ndarray
    _bbox: BoundingBox
    
    def __init__(self, coords: np.ndarray):
        self._coords = np.array(coords, dtype=np.int32)
        self._bbox = self._build_bbox()
    
    @abc.abstractmethod
    def draw(self, img: np.ndarray):
        pass
    
    @abc.abstractmethod
    def _build_bbox(self) -> BoundingBox:
        pass
    
    def collides(self, figure : Self) -> bool:
        box2 = figure.bbox
        box1 = self.bbox
        x1_min, y1_min = min(box1.pt1[0], box1.pt2[0]), min(box1.pt1[1], box1.pt3[1])
        x1_max, y1_max = max(box1.pt1[0], box1.pt2[0]), max(box1.pt1[1], box1.pt3[1])

        x2_min, y2_min = min(box2.pt1[0], box2.pt2[0]), min(box2.pt1[1], box2.pt3[1])
        x2_max, y2_max = max(box2.pt1[0], box2.pt2[0]), max(box2.pt1[1], box2.pt3[1])

        return not (x1_max < x2_min or x1_min > x2_max or
                y1_max < y2_min or y1_min > y2_max)
        
    @property
    def bbox(self):
        return self._bbox
    
    @bbox.setter
    def bbox(self, value):
        self._bbox = value
    
    @property
    def coords(self):
        return self._coords
    
    @coords.setter
    def coords(self, value):
        self._coords = value
        self._bbox = self._build_bbox()