import pytest
from rebox.elements import *

# xyxy, xcycwh, xmymwh
# rel abs

image_width = 200
image_height = 100

@pytest.fixture
def example_xyxy_rel():
    return np.array([0.1,0.2,0.5,0.6])

@pytest.fixture
def example_xyxy_abs():
    return np.array([0.1,0.2,0.5,0.6])

@pytest.fixture
def example_xcycwh_rel():
    return np.array([0.1,0.2,0.5,0.6])

@pytest.fixture
def example_xcycwh_abs():
    return np.array([0.1,0.2,0.5,0.6])

@pytest.fixture
def example_xmymwh_rel():
    return np.array([0.1,0.2,0.5,0.6])

@pytest.fixture
def example_xmymwh_abs():
    return np.array([0.1,0.2,0.5,0.6])
