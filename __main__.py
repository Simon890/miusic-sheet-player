from figures.Rectangle import Rectangle
import numpy as np
import matplotlib.pyplot as plt
from figures.Circle import Circle
from figures.Triangle import Triangle
from trans.Rotation import Rotation

img = np.ones(shape=(128, 128), dtype=np.int32) * 255

rect = Rectangle([[5, 5], [30, 30]])
img = rect.draw(img)
circle = Circle([[100, 100]], 5)
# img = circle.draw(img)
triangle = Triangle([
    [50, 50],
    [50, 90],
    [120, 80]
])
rot = Rotation()
rect_rotado = rot.apply(rect)
print(rect_rotado)
# print(circle.get_bounding_box(), circle.get_bbox_center())
# print(triangle.get_bounding_box())
# img = triangle.draw(img)
# img = rect.draw_bounding_box(img)
# print(rect.get_bounding_box())
plt.imshow(img, cmap="gray")
plt.show()