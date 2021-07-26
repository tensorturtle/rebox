"""2D bounding box module"""

from copy import deepcopy
import numpy as np

from .format import BBoxFormat
from .common_formats import yolo, coco, pascal, albumentations, label_studio

class BBox2D:
    """
    Class to represent a 2D bounding box.

    Args:
        x: Sequence of length 4 representing bounding box coordinates.
        format: :py:class:BBoxFormat corresponding to format of x

    Raises:
        ValueError: If 'box' is not of length 4
        TypeError: If 'box' is not of type {list, tuple, numpy.ndarray, BBox2D

    """
    def __init__(self, x, format:BBoxFormat):
        if isinstance(x, BBox2D):
            x = x.numpy(mode=mode)

        elif isinstance(x, (list, tuple)):
            if len(x) != 4:
                raise ValueError(
                    "Invalid input length. Input should have 4 elements.")
            x = np.asarray(x)

        elif isinstance(x, np.ndarray):
            if x.ndim >= 2:
                x = x.flatten()
            if x.size != 4:
                raise ValueError(
                    "Invalid input length. Input should have 4 elements.")
        else:
            raise TypeError(
                "Expected input to constructor to be a 4 element "
                "list, tuple, numpy ndarray, or BBox2D object.")

        self._format = format
        self._value = x

    # basic magic methods
    def __repr__(self):
        return f"BBox2D({self.value}, BBoxFormat({self.format.style}, {self.format.scale}))"

    def __str__(self):
        print(self.format.scale)
        return f"bbox: {self.value}, format style: {self.format.style}, format scale: {self.format.scale}"

    # Python magic methods

    def __eq__(self, other):
        """
        Strict equals.
        Bounding box value and format must both match.
        """
        raise NotImplementedError
    def __and__(self, other):
        """
        Return new bounding box that is the rectangular intersection between two given bounding boxes.
        """
        raise NotImplementedError
    def __or__(self, other):
        """
        Return new bounding box that contains the union of both bounding boxes tightly.
        """
        raise NotImplementedError
    def __round__(self):
        """
        Round values of bounding box to nearest integer.
        """
        raise NotImplementedError


    @property
    def format(self):
        return self._format

    @property
    def value(self):
        """
        Value of length 4 that represents bounding box.
        Order and meaning of values depend on format.
        """
        return self._value

    @property
    def x1(self):
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[0]
        else:
            raise AttributeError("x1 attribute not available for format: f{self.format}")

    @x1.setter
    def x1(self, value):
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[0] = value
        else:
            raise AttributeError("x1 attribute not available for format: f{self.format}")

    @property
    def x2(self):
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[2]
        else:
            raise AttributeError("x2 attribute not available for format: f{self.format}")

    @x2.setter
    def x2(self, value):
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[2] = value
        else:
            raise AttributeError("x1 attribute not available for format: f{self.format}")

    @property
    def xc(self):
        if self.format.style in ["XcYcWH"]:
            return self.value[0]
        else:
            raise AttributeError("x_center attribute not available for format: f{self.format}")

    @xc.setter
    def xc(self, value):
        if self.format.style in ["XcYcWH"]:
            self.value[0] = value
        else:
            raise AttributeError("x_center attribute not available for format: f{self.format}")

    @property
    def y1(self):
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[1]
        else:
            raise AttributeError("y1 attribute not available for format: f{self.format}")

    @y1.setter
    def y1(self, value):
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[1] = value
        else:
            raise AttributeError("y1 attribute not available for format: f{self.format}")

    @property
    def y2(self):
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[3]
        else:
            raise AttributeError("y2 attribute not available for format: f{self.format}")

    @y2.setter
    def y2(self, value):
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[3] = value
        else:
            raise AttributeError("y2 attribute not available for format: f{self.format}")

    @property
    def yc(self):
        if self.format.style in ["XcYcWH"]:
            return self.value[1]
        else:
            raise AttributeError("y_center attribute not available for format: f{self.format}")

    @yc.setter
    def yc(self, value):
        if self.format in ["XcYcWH"]:
            self.value[1] = value
        else:
            raise AttributeError("y_center attribute not available for format: f{self.format}")

    @property
    def w(self):
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            return self.value[2]
        else:
            raise AttributeError("width not available for format: f{self.format}")

    @w.setter
    def w(self, value):
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            self.value[2] = value
        else:
            raise AttributeError("width not available for format: f{self.format}")

    @property
    def h(self):
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            return self.value[3]
        else:
            raise AttributeError("height not available for format: f{self.format}")

    @h.setter
    def h(self, value):
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            self.value[3] = value
        else:
            raise AttributeError("height not available for format: f{self.format}")

if __name__ == "__main__":
    bbox = BBox2D([15,20,40,50], label_studio)
    print(bbox)
    print(bbox.format)
    print(bbox.format.style)
    print(bbox.value)
