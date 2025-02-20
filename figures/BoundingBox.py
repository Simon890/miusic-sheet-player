import numpy as np

class BoundingBox:
    pt1: np.ndarray
    pt2: np.ndarray
    pt3: np.ndarray
    pt4: np.ndarray
    width: int
    height: int
    center: np.ndarray
    
    def __init__(self, coords : np.ndarray):
        self._coords = coords
        self.pt1 = coords[0]
        self.pt2 = coords[1]
        self.pt3 = coords[2]
        self.pt4 = coords[3]
        self.width = int(np.abs(self.pt1[0] - self.pt2[0]))
        self.height = int(np.abs(self.pt1[1] - self.pt3[1]))
        self.center = np.array([self.pt1[0] + self.width // 2, self.pt1[1] + self.height // 2], dtype=np.float32)
    
    