import pytest
import numpy as np
from rebox import BBoxFormat
from rebox import BBox
from rebox.formats import coco, yolo, pascal, albumentations, label_studio

style_xyxy = "XYXY"
style_xmymwh = "XmYmWH"

# coco example input
@pytest.fixture
def coco_example():
    return BBox([10,20,30,30],coco)
