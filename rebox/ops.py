import numpy as np
from rebox import BBox
from rebox import BBoxFormat

def iou(a, b):
    """
    Compute the Jaccarrd Index / Intersection over Union of a pair of 2D bounding boxes.

    Args:
        a: BBox object
        b: BBox object

    Returns:
        The IoU of the two bounding boxes.
    """

    # dealing with various formats:
    # unify style to XYXY,
    # keep scale, and account for it in algorithm

    assert a.format.style != b.format.style, "IoU calculation not implemented for bounding boxes of different formats. Please convert the two BBoxes to the same format before calculating iou()."

    scale = a.format.scale
    style = a.format.style

    unified_format = BBoxFormat(style, scale)

    a = a.to_format(unified_format)
    b = b.to_format(unified_format)

    xA = np.maximum(a.x1, b.x1)
    yA = np.maximum(a.y1, b.y1)
    xB = np.maximum(a.x2, b.x2)
    yB = np.maximum(a.y2, b.y2)

    if scale is None:
        inter_w = xB - xA + 1
    else:
        inter_w = xB - xA

    inter_w = inter_w * (inter_w >= 0)

    if scale is None:
        inter_h = yB - yA + 1
    else:
        inter_h = yB - yA

    inter_h = inter_h * (inter_h >= 0)

    intersection = inter_w * inter_h

    a_area = a.width * a.height
    b_area = b.width * b.height

    iou = intersection / (a_area + b_area - intersection)

    if np.isinf(iou) or np.isnan(iou):
        iou = 0

    return iou






