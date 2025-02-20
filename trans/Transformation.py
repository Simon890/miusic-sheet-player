import abc
import numpy as np
from figures.Figure import Figure

class Transformation(abc.ABC):
    @abc.abstractmethod
    def apply(self, figure : Figure):
        pass