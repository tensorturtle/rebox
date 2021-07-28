import pytest
import numpy as np
from rebox import BBox
from rebox.formats import coco

x1 = 10
y1 = 20
w = 30
h = 40

x1_alt = 15
y1_alt = 25
w_alt = 35
h_alt = 45

# coco example input
@pytest.fixture
def coco_example():
    return BBox([x1,y1,w,h],coco)

@pytest.fixture
def value_example():
    return np.array([x1,y1,w,h])

@pytest.fixture
def value_alt_example():
    return np.array([x1_alt, y1_alt, w_alt, h_alt])

def test_repr(coco_example):
    assert repr(coco_example) == f"BBox([{x1} {y1} {w} {h}], BBoxFormat(XmYmWH, None))"

def test_str(coco_example):
    assert str(coco_example) == f"Coordinates: [{x1} {y1} {w} {h}], Style: XmYmWH, Scale: None"

def test_get_format(coco_example):
    assert coco_example.format.style == "XmYmWH"

def test_get_value(coco_example, value_example):
    assert np.array_equal(coco_example.value, value_example)

def test_set_value(coco_example, value_alt_example):
    coco_example.value = value_alt_example
    assert np.array_equal(coco_example.value, value_alt_example)

def test_get_x1_attribute(coco_example):
    assert coco_example.x1 == x1

def test_set_x1_attribute(coco_example):
    coco_example.x1 = x1_alt
    assert coco_example.x1 == x1_alt

def test_get_y1_attribute(coco_example):
    assert coco_example.y1 == y1

def test_set_y1_attribute(coco_example):
    coco_example.y1 = y1_alt
    assert coco_example.y1 == y1_alt

def test_get_w_attribute(coco_example):
    assert coco_example.w == w

def test_set_w_attribute(coco_example):
    coco_example.w = w_alt
    assert coco_example.w == w_alt

def test_get_h_attribute(coco_example):
    assert coco_example.h == h

def test_set_h_attribute(coco_example):
    coco_example.h = h_alt
    assert coco_example.h == h_alt

def test_get_x2_attribute(coco_example):
    with pytest.raises(AttributeError):
        coco_example.x2

def test_set_x2_attribute(coco_example):
    with pytest.raises(AttributeError):
        coco_example.x2 = 1

def test_get_y2_attribute(coco_example):
    with pytest.raises(AttributeError):
        coco_example.y2

def test_set_y2_attribute(coco_example):
    with pytest.raises(AttributeError):
        coco_example.y2 = 1

def test_get_xc_attribute(coco_example):
    with pytest.raises(AttributeError):
        coco_example.xc

def test_set_xc_attribute(coco_example):
    with pytest.raises(AttributeError):
        coco_example.xc = 1

def test_get_yc_attribute(coco_example):
    with pytest.raises(AttributeError):
        coco_example.yc

def test_set_yc_attribute(coco_example):
    with pytest.raises(AttributeError):
        coco_example.yc = 1


