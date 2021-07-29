import pytest
import numpy as np
from rebox import BBoxFormat
from rebox import BBox
from rebox.formats import coco, yolo, pascal, albumentations, label_studio

style_xyxy = "XYXY"
style_xmymwh = "XmYmWH"
style_xcycwh = "XcYcWH"

# COCO
def test_coco_style_attribute():
    assert coco.style == style_xmymwh

def test_coco_scale_attribute():
    assert coco.scale == None

def test_coco_is_relative_attribute():
    assert coco.is_relative == False

# YOLO
def test_yolo_style_attribute():
    assert yolo.style == style_xcycwh

def test_yolo_scale_attribute():
    assert yolo.scale == 1

def test_yolo_is_relative_attribute():
    assert yolo.is_relative == True

# PASCAL_VOC
def test_pascal_style_attribute():
    assert pascal.style == style_xyxy

def test_pascal_scale_attribute():
    assert pascal.scale == None

def test_pascal_is_relative_attribute():
    assert pascal.is_relative == False

# Albumentations
def test_a_style_attribute():
    assert albumentations.style == style_xyxy

def test_a_scale_attribute():
    assert albumentations.scale == 1

def test_a_is_relative_attribute():
    assert albumentations.is_relative == True

# Label Studio
def test_label_studio_style_attribute():
    assert label_studio.style == style_xmymwh

def test_label_studio_scale_attribute():
    assert label_studio.scale == 100

def test_label_studio_is_relative_attribute():
    assert label_studio.is_relative == True
