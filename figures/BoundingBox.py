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
    category: int
    
    def __init__(self, pt1: np.ndarray, pt2: np.ndarray, pt3: np.ndarray, pt4: np.ndarray, category:int):
        self.pt1 = np.array(pt1)
        self.pt2 = np.array(pt2)
        self.pt3 = np.array(pt3)
        self.pt4 = np.array(pt4)
        self.width = int(np.abs(self.pt1[0] - self.pt2[0]))
        self.height = int(np.abs(self.pt1[1] - self.pt3[1]))
        self.centroid = np.array([self.pt1[0] + self.width // 2, self.pt1[1] + self.height // 2], dtype=np.float32)
        self.coords = np.array([self.pt1, self.pt2, self.pt3, self.pt4])
        self.category = category
    
    def draw(self, img : np.ndarray):
        return cv2.rectangle(img, self.pt1, self.pt3, 120)
    
    def to_str(self):
        scaled_pt1 = self.pt1 / 128
        scaled_pt2 = self.pt2 / 128
        scaled_pt3 = self.pt3 / 128
        scaled_pt4 = self.pt4 / 128
        return f"{self.category} {scaled_pt1[0]} {scaled_pt1[1]} {scaled_pt2[0]} {scaled_pt2[1]} {scaled_pt3[0]} {scaled_pt3[1]} {scaled_pt4[0]} {scaled_pt4[1]}"
    