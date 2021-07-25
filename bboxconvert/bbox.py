"""2D bounding box module"""

from copy import deepcopy
import numpy as np

from format import BBoxFormat

# common research bounding box annotation formats
yolo_format = BBoxFormat(style='XcYcWH', scale=1)
coco_format = BBoxFormat(style='XmYmWH', scale=None)
pascal_voc_format = BBoxFormat(style='XYXY', scale=None)
albumentations_format = BBoxFormat(style='XYXY', scale=1)
label_studio_format = BBoxFormat(style='XmYmWH', scale=100)

class BBox2D:
    """
    Class to represent a 2D bounding box.

    Args:
        box: Sequence of length 4 representing bounding box coordinates.
        mode: User-defined bbox format and scaling. This is only loosely coupled with 'box'. This class will not enforce or check that the 'box' is in the correct 'mode' format. Create your own BBoxFormat or choose among built-in popular formats: 'yolo','coco','pascal_voc','albumentations','label_studio'.
        manual_scaling: if mode not entered, choose relative scaling factor (0 for absolute pixel values, 1 for normalizing between 0 and 1, 100 for percentage)

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

        self._format = format # validate that 'box' conforms to possible limits of 'format'
        self._value = x # length


    def __eq__(self,x):
        raise NotImplementedError
    def __and__(self, other):
        #return bbox that is self AND other
        raise NotImplementedError
    def __or__(self, other):
        #return rectangular bbox that contains both self and other
        raise NotImplementedError
    def __round__(self):
        # round to integer
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

if __name__ == "__main__":
    bbox = BBox2D([15,20,40,50], label_studio_format)
    print(bbox)
    print(bbox.format)
    print(bbox.format.style)
    print(bbox.value)
