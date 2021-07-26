# bboxconvert

[![CircleCI](https://circleci.com/gh/tensorturtle/bboxconvert.svg?style=shield)](https://app.circleci.com/pipelines/github/tensorturtle/bboxconvert)


Fluidly convert between 2D rectangular bounding box annotation formats in Python.

Like [varunagrawal/bbox](https://github.com/varunagrawal/bbox)
  + ❌ only 2D bounding boxes are supported
  + 🟢 add many more built-in 'real world' annotation formats
  + 🟢 add ability to create your own.


A lot of object detection codebases have their own bounding box manipulation utility functions. Don't Repeat Yourself and use this instead.

## Installation

Install with pip:
```
pip install bboxconvert
```

## Usage

Example: converting from YOLO-style to COCO-style bounding box format.

```python3
from bboxconvert import BBox2D, BBoxFormat, bboxconvert

image_height = 360 # pixels
image_width = 640 # pixels

yolo_bbox = BBox2D([0.31, 0.5, 0.2, 0.6], yolo_format) # using built-in 'yolo_format'

coco_bbox = bboxconvert(yolo_bbox, coco_format) # using built-in 'coco_format'
```

Common formats such as YOLO, COCO, PASCAL_VOC, Albumentations, and Label Studio are provided as a convenience. If you wish to make your own coordinates format, instantiate the BBoxFormat class.


### Common Bounding Box Formats

|                	|               Scale              	|           Style          	|
|--------------:	|:--------------------------------:	|:-------------------------------------:	|
|      **YOLO**      	|         Normalized [0,1]         	| `[ x_Center, y_Center, width, height ]` 	|
|      **COCO**      	| Pixels [0, width] or [0, height] 	|    `[ x_min, y_min, width, height ]`    	|
|   **PASCAL_VOC**   	| Pixels [0, width] or [0, height] 	|     `[ x_min, y_min, x_MAX, y_MAX ]`    	|
| **Albumentations** 	|         Normalized [0,1]         	|     `[x_min, y_min, x_MAX, y_MAX ]`    	|
| **Label Studio**    | Normalized percentage [0, 100]    |     `[x_min, y_min, width, height]`     |
