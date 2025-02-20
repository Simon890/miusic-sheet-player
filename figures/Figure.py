import abc
import cv2
import numpy as np
from typing_extensions import Self
from figures.BoundingBox import BoundingBox

class Figure(abc.ABC):
    
    _coords: list
    _bbox: BoundingBox
    
    def __init__(self, coords: list):
        self._coords = coords
        self._bbox = BoundingBox(self._coords)
    
    @abc.abstractmethod
    def draw(self, img: np.ndarray):
        pass
    
    @abc.abstractmethod
    def get_bounding_box(self) -> np.ndarray:
        pass
    
    def get_bbox_center(self) -> np.ndarray:
        pt1, pt2, pt3, pt4 = self.get_bounding_box()
        width = np.abs(pt1[0] - pt2[0])
        height = np.abs(pt1[1] - pt3[1])
        return np.array([pt1[0] + width // 2, pt1[1] + height // 2], dtype=np.float32)
    
    def draw_bounding_box(self, img: np.ndarray) -> np.ndarray:
        bbox_coords = self.get_bounding_box()
        return cv2.rectangle(img, bbox_coords[0], bbox_coords[2], 100)
    
    def collides(self, figure : Self) -> bool:
        figure._coords