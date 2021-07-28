import pytest
import numpy as np
from rebox import BBoxFormat
from rebox import BBox
from rebox.formats import coco, yolo, pascal, albumentations, label_studio

style_xyxy = "XYXY"
style_xmymwh = "XmYmWH"
style_xcycwh = "XcYcWH"


# COCO
def test_style_attribute():
    assert coco.style == style_xmymwh

def test_scale_attribute():
    assert coco.scale == None

def test_is_relative_attribute():
    assert coco.is_relative == False

# YOLO
def test_style_attribute():
    assert yolo.style == style_xcycwh

def test_scale_attribute():
    assert coco.scale == 1

def test_is_relative_attribute():
    assert coco.is_relative == True

# PASCAL_VOC
def test_style_attribute():
    assert pascal.style == style_xyxy

def test_scale_attribute():
    assert pascal.scale == None

def test_is_relative_attribute():
    assert pascal.is_relative == False

# Albumentations
def test_style_attribute():
    assert albumentations.style == style_xyxy

def test_scale_attribute():
    assert albumentations.scale == 1

def test_is_relative_attribute():
    assert albumentations.is_relative == True


# Label Studio
def test_style_attribute():
    assert label_studio.style == style_xmymwh

def test_scale_attribute():
    assert label_studio.scale == 100

def test_is_relative_attribute():
    assert label_studio.is_relative == True
