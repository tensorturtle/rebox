"""2D bounding box format converter module

Use example:
converter = BBoxConverter(from='coco', to='yolo')
yolo_bbox = converter(coco_bbox)
"""

import numpy as np
from elements import *
from bbox import *
from format import BBoxFormat

def _validate_image_size(image_width, image_height):
    if image_width is None or image_height is None:
        raise ValueError("Must enter 'image_width' and 'image_height' when converting across absolute and relative formats.")
    if image_width <= 0 or image_height <= 0:
        raise ValueError("Image width and height must be greater than zero.")


def _style_import(bbox: BBox2D) -> BBox2D:
    """
    Convert 'bbox' to XYXY format, keeping scale unchanged.
    """
    if bbox.format.is_relative:
        if bbox.format.style == "XmYmWH":
            output = XmYmWH_to_XYXY(bbox.value)
        elif bbox.format.style == "XcYcWH":
            output = XcYcWH_to_XYXY(bbox.value)
        elif bbox.format.style == "XYXY":
            output = bbox.value
        else:
            raise ValueError("Invalid format style given. Check format of bounding box.")
    else: # absolute format (counting in whole pixels); account for fencepost error
        if bbox.format.style == "XmYmWH":
            output = pixel_XmYmWH_to_XYXY(bbox.value)
        elif bbox.format.style == "XcYcWH":
            output = pixel_XcYcWH_to_XYXY(bbox.value)
        elif bbox.format.style == "XYXY":
            output = bbox.value

    xyxy_format_same_scale = BBoxFormat("XYXY", bbox.format.scale) # only style was changed. Scale was not changed.

    return BBox2D(output, xyxy_format_same_scale)


def _style_export(bbox: BBox2D, target_format: BBoxFormat) -> BBox2D: # keeps scale intact
    """
    Convert the format of 'bbox', the preferred universal internal representation, to 'target_format', without changing scale.
    """

    if bbox.format.is_relative:
        if target_format.style == "XmYmWH":
            output = XYXY_to_XmYmWH(bbox.value)
        elif target_format.style == "XcYcWH":
            output = XYXY_to_XcYcWH(bbox.value)
        elif target_format.style == "XYXY":
            output = bbox.value
        else:
            raise ValueError("Invalid format style given. Check format of bounding box.")
    else: # absolute format; account for fencepost error
        if target_format.style == "XmYmWH":
            output = pixel_XYXY_to_XmYmWH(bbox.value)
        elif target_format.style == "XcYcWH":
            output = pixel_XYXY_to_XcYcWH(bbox.value)
        elif target_format.style == "XYXY":
            output = bbox.value

    output_format = BBoxFormat(target_format.style, target_format.scale)
    return BBox2D(output, output_format)


def convert(source_bbox: BBox2D, target_format: BBoxFormat, image_width=None, image_height=None) -> BBox2D:

    # strategy for managing combinatorial growth in conversions
    # use interim XYXY style

    # 1. convert input to XYXY style interim format without touching scale
    interim_bbox = _style_import(source_bbox)

    # 2. Apply scale conversion
    if source_bbox.format.is_relative != target_format.is_relative:
        _validate_image_size(image_width, image_height) # require image size if converting across absolute/relative formats
        if source_bbox.format.is_relative:
            # converting from relative to absolute
            interim_bbox = BBox2D(xyxy_scaled_rel_to_abs(interim_bbox.value, interim_bbox.format.scale, image_width, image_height), source_bbox.format)
        else:
            # converting from absolute to relative
            interim_bbox = BBox2D(xyxy_abs_to_scaled_rel(interim_bbox.value, interim_bbox.format.scale, image_width, image_height), source_bbox.format)


    # 3. Convert style from interim format to desired format
    target_bbox = _style_export(interim_bbox, target_format)

    return target_bbox

if __name__ == "__main__":
    example1 = BBox2D([120,115,40,50], coco_format)
    print(example1)

    converted_example1 = convert(example1, label_studio_format, 10,10)

    print(converted_example1.value)
    print(converted_example1.format.style)
    print(converted_example1.format.scale)
