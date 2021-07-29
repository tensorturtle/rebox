import pytest
from rebox.elements import XcYcWH_to_XYXY, XYXY_to_XcYcWH, XmYmWH_to_XYXY, XYXY_to_XmYmWH, normalize, denormalize, xyxy_scaled_rel_to_abs, xyxy_abs_to_scaled_rel, xyxy_simple_rescale

# xyxy, xcycwh, xmymwh
# rel abs

image_width = 200
image_height = 100

@pytest.fixture
def example_xyxy_rel():
    return np.array([0.1,0.2,0.5,0.6])

@pytest.fixture
def example_xyxy_abs():
    return np.array([20,20,100,60])

@pytest.fixture
def example_xcycwh_rel():
    return np.array([0.3,0.4,0.4,0.4])

@pytest.fixture
def example_xcycwh_abs():
    return np.array([60,40,80,60])

@pytest.fixture
def example_xmymwh_rel():
    return np.array([0.1,0.2,0.4,0.4])

@pytest.fixture
def example_xmymwh_abs():
    return np.array([20,20,80,40])

def test_xcycwh_to_xyxy_rel(example_xcycwh_rel):
    assert np.array_equal(XcYcWH_to_XYXY(example_xcycwh_rel), example_xyxy_rel)

def test_xcycwh_to_xyxy_abs(example_xcycwh_abs):
    assert np.array_equal(XcYcWH_to_XYXY(example_xcycwh_abs), example_xyxy_rel)

def test_xyxy_to_xcycwh_rel(example_xyxy_rel):
    assert np.array_equal(XYXY_to_XcYcWH(example_xyxy_rel), example_xcycwh_rel)

def test_xyxy_to_xcycwh_abs(example_xyxy_abs):
    assert np.array_equal(XYXY_to_XcYcWH(example_xyxy_abs), example_xcycwh_abs)

def test_xmymwh_to_xyxy_rel(example_xmymwh_rel):
    assert np.array_equal(XmYmWH_to_XYXY(example_xmymwh_rel), example_xyxy_rel)

def test_xmymwh_to_xyxy_abs(example_xmymwh_abs):
    assert np.array_equal(XmYmWH_to_XYXY(example_xmymwh_abs), example_xyxy_abs)

def test_xyxy_to_xmymwh_rel(example_xyxy_rel):
    assert np.array_equal(XYXY_to_XmYmWH(example_xyxy_rel), example_xmymwh_rel)

def test_xyxy_to_xmymwh_abs(example_xyxy_abs):
    assert np.array_equal(XYXY_to_XmYmWH(example_xyxy_abs), example_xmymwh_abs)

