# rebox: Easily convert between bounding box formats

[![Build](https://github.com/tensorturtle/rebox/actions/workflows/build.yml/badge.svg)](https://github.com/tensorturtle/rebox/actions)
[![codecov](https://codecov.io/gh/tensorturtle/rebox/branch/main/graph/badge.svg?token=H7HTDYNIAV)](https://codecov.io/gh/tensorturtle/rebox) 
[![codacy](https://img.shields.io/codacy/grade/b16458c671284c5e98c65e6124ad4c79)](https://app.codacy.com/gh/tensorturtle/rebox/dashboard)

Fluidly convert between 2D rectangular bounding box annotation formats.

Instead of writing yet more utility functions to convert between bounding box formats and perform common operations using them, use this instead.

There's nothing magical about this package, it really is just meant to replace boilerplate code.

## Quickstart

**Install with pip:**
```bash
pip install rebox
```

**Convert a bounding box from COCO format to VOC_PASCAL format**:
```py
>> from rebox import BBox
>> from rebox.formats import coco, pascal

>> coco_bbox = BBox([40,50,20,15], coco)
>> pascal_bbox = coco_bbox.as_format(pascal)

>> pascal_bbox
"Coordinates: [40 50 59 64], Style: XYXY, Scale: None"

>> pascal_bbox.value
[40 50 59 64]
```

## Supported Bounding Box Formats

Common formats such as YOLO, COCO, PASCAL_VOC, Albumentations, and Label Studio are provided as a convenience. If you wish to make your own coordinates format, instantiate the BBoxFormat class.

|                	|               Scale              	|           Style          	|
|--------------:	|:--------------------------------:	|:-------------------------------------:	|
|      **YOLO**      	|         Normalized (0,1)        	| `[ x_Center, y_Center, width, height ]` 	|
|      **COCO**      	| Pixels                         	|    `[ x_min, y_min, width, height ]`    	|
|   **PASCAL_VOC**   	| Pixels                         	|     `[ x_min, y_min, x_MAX, y_MAX ]`    	|
| **Albumentations** 	|         Normalized (0,1)         	|     `[x_min, y_min, x_MAX, y_MAX ]`    	|
| **Label Studio**    | Normalized percentage (0, 100)    |     `[x_min, y_min, width, height]`     |

Inspired by [varunagrawal/bbox](https://github.com/varunagrawal/bbox). `bbox` is not flexible enough to accomodate the various format schemes.

## Usage

### Creating a `BBox` and access/modifing its attributes

```py
# readme_examples/create_bbox.py

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

### Converting between the same absolute/relative formats

The simplest conversion keeps the same scale, but with different styles:

```py
# readme_examples/simple_conversion.py

from rebox import BBox
from rebox.formats import coco, pascal

coco_bbox = BBox([40,50,20,15], coco)
pascal_bbox = coco_bbox.as_format(pascal)

print(pascal_bbox) # "Coordinates: [40 50 59 64], Style: XYXY, Scale: None"
print(pascal_bbox.value) # [40 50 59 64]

```

### Converting across absolute/relative formats

This time, pass in image height and width, to convert across pixel values and relative scale values.

```py
# readme_examples/absolute_relative_conversion.py

from rebox import BBox
from rebox.formats import yolo, coco

image_height = 360 # pixels
image_width = 640 # pixels

yolo_bbox = BBox([0.31, 0.5, 0.2, 0.6], yolo) # using built-in 'yolo_format'

coco_bbox = yolo_bbox.as_format(coco, image_width, image_height) # to convert to built-in format 'coco'

print(coco_bbox.value) # array([134.4,  72. , 128. , 216. ])

```

### Operations on `BBox`es

`rebox` includes several common utility operations on bounding boxes.

#### IOU (Intersection over Union) of two bounding boxes

```py
# readme_examples/iou.py

from rebox import BBox
from rebox.formats import coco, pascal
from rebox.ops import iou

one_bbox = BBox([40,50,20,10], coco)
two_bbox = BBox([45,60, 30, 20], pascal)

iou = iou(one_bbox, two_bbox)

```

If you would like to see more operations, please submit an Issue.

## Development 

I organized often-used commands into scripts.

`bump_0.1_patch.sh` increments the 'patch' version (last place)

`pypi_build.sh` creates a new distro wheel

`pypi_upload.sh` uses twine to upload to pypi

`testpypi_upload.sh` is for uploading to test pypi
