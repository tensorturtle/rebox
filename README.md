# rebox

[![Build](https://github.com/tensorturtle/rebox/actions/workflows/build.yml/badge.svg)](https://github.com/tensorturtle/rebox/actions)
[![codecov](https://codecov.io/gh/tensorturtle/rebox/branch/main/graph/badge.svg?token=H7HTDYNIAV)](https://app.codecov.io/gh/tensorturtle/rebox)
[![codacy](https://img.shields.io/codacy/grade/b16458c671284c5e98c65e6124ad4c79)](https://app.codacy.com/gh/tensorturtle/rebox/dashboard)

## Bounding boxes done right

**WARNING: CURRENTLY IN ALPHA DEVELOPMENT**

Fluidly convert between native representations of 2D rectangular bounding box annotation formats in Python.

Instead of writing yet more utility functions to convert between bounding box formats, use this instead.

> **Like [varunagrawal/bbox](https://github.com/varunagrawal/bbox), but**
> +   ⚠️ only support 2D bounding boxes
> +   ✅ add several built-in 'real world' annotation formats
> +   ✅ add ability to create and use your own annotation format

## Installation

Install with pip:

![Oh no](https://github.com/tensorturtle/rebox/blob/cf6260950e9a85245d1f8e1e1e907f86975870ac/readme_examples.py#L1-L15)

## Usage

### Level 0: Create a `BBox` and access/modify its attributes

```python:examples/bbox_creation.py
```

```python3
from rebox import BBox
from rebox.formats import coco

coco_bbox = BBox([40,50,20,15], coco)

print(coco_bbox.format.style) # XmYmWH
print(coco_bbox.format.scale) # None
print(coco_bbox.x1) # 40
print(coco_bbox.y1) # 50
print(coco_bbox.w) # 20
print(coco_bbox.h) # 15

# set values
coco_bbox.x1 = 60
print(coco_bbox.x1) # 60
```

These attributes are only implemented for the current format,
and are not automatically converted. For example, trying to access `x2` for a `XmYmWH` format returns `AttributeError`.

### Level 1: Converting between the same absolute/relative formats

The simplest conversion keeps the same scale, but with different styles:

```python3
from rebox import BBox
from rebox.formats import coco, pascal

coco_bbox = BBox([40,50,20,15], coco)
pascal_bbox = coco_bbox.as_format(pascal)

print(pascal_bbox) # "Coordinates: [40 50 59 64], Style: XYXY, Scale: None"
print(pascal_bbox.value) # [40 50 59 64]
```

### Level 2: Converting across absolute/relative formats

This time, pass in image height and width, to convert across pixel values and relative scale values.

```python3
from rebox import BBox
from rebox.formats import yolo, coco

image_height = 360 # pixels
image_width = 640 # pixels

yolo_bbox = BBox([0.31, 0.5, 0.2, 0.6], yolo) # using built-in 'yolo_format'

coco_bbox = yolo_bbox.as_format(coco, image_width, image_height) # to convert to built-in format 'coco'

print(coco_bbox.value) # array([134.4,  72. , 128. , 216. ])
```

### Level 3: Operations on `BBox`es

`rebox` includes several common utility operations on bounding boxes.

#### IOU (Intersection over Union) of two bounding boxes

```python3
from rebox import BBox
from rebox.formats coco, pascal
from rebox.ops import IOU

one_bbox = BBox([40,50,20,10], coco)
two_bbox = BBox([45,60, 30, 20], pascal)

iou = IOU(one_bbox, two_bbox)
```

### Common Bounding Box Formats

Common formats such as YOLO, COCO, PASCAL_VOC, Albumentations, and Label Studio are provided as a convenience. If you wish to make your own coordinates format, instantiate the BBoxFormat class.

|                	|               Scale              	|           Style          	|
|--------------:	|:--------------------------------:	|:-------------------------------------:	|
|      **YOLO**      	|         Normalized (0,1)        	| `[ x_Center, y_Center, width, height ]` 	|
|      **COCO**      	| Pixels                         	|    `[ x_min, y_min, width, height ]`    	|
|   **PASCAL_VOC**   	| Pixels                         	|     `[ x_min, y_min, x_MAX, y_MAX ]`    	|
| **Albumentations** 	|         Normalized (0,1)         	|     `[x_min, y_min, x_MAX, y_MAX ]`    	|
| **Label Studio**    | Normalized percentage (0, 100)    |     `[x_min, y_min, width, height]`     |
