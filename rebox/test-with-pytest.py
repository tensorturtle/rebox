import pytest
from .bbox import *
from .format import *
from .converter import bboxconvert
from .elements import *
import numpy as np

# example input data
@pytest.fixture
def center_quarter_area_bbox():
    return BBox2D([100,200,300,400], coco_format)

def test_coco_to_voc(center_quarter_area_bbox):
    voc_bbox = bboxconvert(center_quarter_area_bbox, pascal_voc_format)
    answer = np.array([100,200,399,599])
    assert np.array_equal(voc_bbox.value, answer)
