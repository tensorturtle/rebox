import pytest
import numpy as np
from rebox import BBox
from rebox.formats import coco, yolo, pascal, albumentations, label_studio

# coco example input
@pytest.fixture
def coco_example():
    return BBox([10,20,30,30],coco)

def test_value(coco_example):
    assert np.array_equal(coco_example.value, np.array([10,20,30,30]))
