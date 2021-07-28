import pytest
import numpy as np
from rebox import BBoxFormat
from rebox import BBox
from rebox.formats import coco, yolo, pascal, albumentations, label_studio

style_xyxy = "XYXY"
style_xmymwh = "XmYmWH"
style_xcycwh = "XcYcWH"

def test_style_attribute():
    assert coco.style == style_xmymwh

def test_scale_attribute():
    assert coco.scale == None

def test_is_relative_attribute():
    assert coco.is_relative == True

