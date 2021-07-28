import pytest
from rebox import BBoxFormat

@pytest.fixture
def example_format():
    return BBoxFormat("XYXY", 10)

def test_style(example_format):
    assert example_format.style == "XYXY"

def test_scale(example_format):
    assert example_format.scale == 10

def test_is_relative(example_format):
    assert example_format.is_relative == True
