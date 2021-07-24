"""2D bounding box module"""

from copy import deepcopy
import numpy as np

class BBox2D:
    """
    Class to represent a 2D bounding box.

    Args:
        box: Sequence of length 4 representing bounding box coordinates.
        mode: Pre-configured bbox format and scaling, choose among: 'yolo','coco','pascal_voc','albumentations','label_studio'
        manual_format: if mode not entered, choose bbox format among: 'xcycwh', 'xmymwh', 'xyxy'
        manual_scaling: if mode not entered, choose relative scaling factor (0 for absolute pixel values, 1 for normalizing between 0 and 1, 100 for percentage)

    Raises:
        ValueError: If 'box' is not of length 4
        TypeError: If 'box' is not of type {list, tuple, numpy.ndarray, BBox2D

    """
    def __init__(self, box, mode='yolo', manual_format=None, manual_scaling=None):
        """
        The internal representation of BBox2D is equivalent to 'yolo

