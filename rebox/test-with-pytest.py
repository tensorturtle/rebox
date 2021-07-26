import pytest
from .bbox import *
from .format import *
from .common_formats import *
from .elements import *
import numpy as np

# example input data
@pytest.fixture
def center_quarter_area_bbox():
    return BBox2D([100,200,300,400], coco)

def test_coco_to_voc(center_quarter_area_bbox):
    voc_bbox = center_quarter_area_bbox.as_format(pascal)
    answer = np.array([100,200,399,599])
    assert np.array_equal(voc_bbox.value, answer)
