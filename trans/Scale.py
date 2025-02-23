from trans.Transformation import Transformation
import numpy as np
from figures.BoundingBox import BoundingBox

class Scale(Transformation):
    
    __scale = 1
    def __init__(self, scale):
        self.__scale = scale
        super().__init__()
    
    def apply(self, figure):
        scale_mat = np.array([
            [self.__scale, 0],
            [0, self.__scale]
        ])
        coords = np.array(np.dot(figure.bbox.coords - figure.bbox.centroid, scale_mat.T) + figure.bbox.centroid, np.int32)
        figure.bbox = BoundingBox(coords[0], coords[1], coords[2], coords[3])
        