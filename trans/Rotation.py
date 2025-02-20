import cv2
from trans.Transformation import Transformation

class Rotation(Transformation):
    def apply(self, figure):
        center = figure.get_bbox_center()
        print("CENTER", center)
        rot_mat = cv2.getRotationMatrix2D(center, 25, 1)
        return cv2.warpAffine(figure.get_bounding_box(), rot_mat)