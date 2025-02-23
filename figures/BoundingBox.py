import cv2
import numpy as np

class BoundingBox:
    pt1: np.ndarray
    pt2: np.ndarray
    pt3: np.ndarray
    pt4: np.ndarray
    width: int
    height: int
    centroid: np.ndarray
    coords: np.ndarray
    
    def __init__(self, pt1: np.ndarray, pt2: np.ndarray, pt3: np.ndarray, pt4: np.ndarray):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3
        self.pt4 = pt4
        self.width = int(np.abs(self.pt1[0] - self.pt2[0]))
        self.height = int(np.abs(self.pt1[1] - self.pt3[1]))
        self.centroid = np.array([self.pt1[0] + self.width // 2, self.pt1[1] + self.height // 2], dtype=np.float32)
        self.coords = np.array([self.pt1, self.pt2, self.pt3, self.pt4])
    
    def draw(self, img : np.ndarray):
        return cv2.rectangle(img, self.pt1, self.pt3, 120)
    