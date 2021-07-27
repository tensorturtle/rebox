# rebox: IN DEVELOPMENT; NOT READY TO USE

![Build](https://github.com/tensorturtle/rebox/actions/workflows/build.yml/badge.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bb672c0f7b4c4aab9ab8042c07c8f7dc)](https://app.codacy.com/gh/tensorturtle/rebox?utm_source=github.com&utm_medium=referral&utm_content=tensorturtle/rebox&utm_campaign=Badge_Grade_Settings)
[![codecov](https://codecov.io/gh/tensorturtle/rebox/branch/main/graph/badge.svg?token=H7HTDYNIAV)](https://codecov.io/gh/tensorturtle/rebox)



Fluidly convert between 2D rectangular bounding box annotation formats in Python.

Instead of writing yet more utility functions to convert between bounding box formats, use this instead.

> **Like [varunagrawal/bbox](https://github.com/varunagrawal/bbox), but**
> + ⚠️ only support 2D bounding boxes
> + ✅ add several built-in 'real world' annotation formats
> + ✅ add ability to create and use your own annotation format

## Installation

Install with pip:
```
pip install rebox
```

## Usage

Example: converting from YOLO-style to COCO-style bounding box format.

```python3
from rebox import BBox2D

image_height = 360 # pixels
image_width = 640 # pixels

yolo_bbox = BBox2D([0.31, 0.5, 0.2, 0.6], yolo_format) # using built-in 'yolo_format'

coco_bbox = yolo_bbox.as_format(coco, image_width, image_height) # to convert to built-in format 'coco'
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
