# bboxconvert

## WARNING: This package is not ready for use. It is currently in development. Expected release date: 2021-08-01

[![CircleCI](https://circleci.com/gh/tensorturtle/bboxconvert.svg?style=shield)](https://app.circleci.com/pipelines/github/tensorturtle/bboxconvert)

Fluidly convert between 2D rectangular bounding box annotation formats in Python.

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

Common formats such as YOLO, COCO, PASCAL_VOC, Albumentations, and Label Studio are provided already,
but if you wish, you can make your own coordinates format by instantiating the BBoxFormat class.


### Common Bounding Box Formats

|                	|               Scale              	|           Style          	|
|--------------:	|:--------------------------------:	|:-------------------------------------:	|
|      **YOLO**      	|         Normalized [0,1]         	| `[ x_Center, y_Center, width, height ]` 	|
|      **COCO**      	| Pixels [0, width] or [0, height] 	|    `[ x_min, y_min, width, height ]`    	|
|   **PASCAL_VOC**   	| Pixels [0, width] or [0, height] 	|     `[ x_min, y_min, x_MAX, y_MAX ]`    	|
| **Albumentations** 	|         Normalized [0,1]         	|     `[x_min, y_min, x_MAX, y_MAX ]`    	|
| **Label Studio**    | Normalized percentage [0, 100]    |     `[x_min, y_min, width, height]`     |


## Look foward to...

- [ ] Numpy and PyTorch tensor support with vectorized operations
- [ ] Auto batch detection & processing
