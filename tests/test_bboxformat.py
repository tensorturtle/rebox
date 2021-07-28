import pytest
from rebox import BBoxFormat

@pytest.fixture
def example_xyxy_1000_format():
    return BBoxFormat("XYXY", 1000)

def test_style(example_xyxy_1000_format):
    assert example_xyxy_1000_format.style ="XYXY"

def test_scale(example_xyxy_1000_format):
    assert example_xyxy_1000_format.scale == 1000

def test_scale(example_xyxy_1000_format):
    assert example_xyxy_1000_format.is_relative == True

@pytest.fixture
def example_xmymwh_none_format():
    return BBoxFormat("XmYmWH", None)

def test_style(example_xmymwh_none_format):
    assert example_xmymwh_none_format.style == "XmYmWH"

def test_scale(example_xyxy_1000_format):
    assert example_xmymwh_none_format.scale == None

def test_scale(example_xyxy_1000_format):
    assert example_xmymwh_none_format.is_relative == False
