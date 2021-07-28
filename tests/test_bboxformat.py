import pytest
import numpy as np
from rebox import BBoxFormat
from rebox import BBox
from rebox.formats import coco, yolo, pascal, albumentations, label_studio

style_xyxy = "XYXY"
style_xmymwh = "XmYmWH"
style_xcycwh = "XcYcWH"

# coco example input
@pytest.fixture
def coco_example():
    return BBox([10,20,30,30],coco)

def test_style_attribute(coco_example):
    assert coco_example.style == style_xmymwh

def test_scale_attribute(coco_example):
    assert coco_example.scale == None

def test_is_relative_attribute(coco_example):
    assert coco_example.is_relative == True

