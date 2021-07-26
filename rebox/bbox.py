"""2D bounding box module"""

from copy import deepcopy
import numpy as np

from .format import BBoxFormat
from .common_formats import yolo, coco, pascal, albumentations, label_studio
from .elements import XcYcWH_to_XYXY, XYXY_to_XcYcWH, XmYmWH_to_XYXY, XYXY_to_XmYmWH, xyxy_scaled_rel_to_abs, xyxy_abs_to_scaled_rel, xyxy_simple_rescale

class BBox2D:
    """
    Class to represent a 2D bounding box.

    Args:
        x: Sequence of length 4 representing bounding box coordinates.
        format: :py:class:BBoxFormat corresponding to format of x

    Raises:
        ValueError: If 'box' is not of length 4
        TypeError: If 'box' is not of type {list, tuple, numpy.ndarray, BBox2D
    """

    def __init__(self, x, format:BBoxFormat):
        x = self._validate_box(x)
        self._format = format
        self._value = x

    def as_format(self, target_format: BBoxFormat, image_width=None, image_height=None):
        # converting directly between all available formats means combinatorial numbers of operations. Therefore, to simply conversion, we convert 'self' to an interim 'XYXY' style, then apply scale, then convert interim style to target style
        interim = _xyxyify(self)
        scaled_interim = _rescale(interim, target_format, image_width, image_height)
        target_bbox = _restyle(scaled_interim, target_format)
        return target_bbox

    # helper for self.to_format()
    def _restyle(bbox: BBox2D, target_format: BBoxFormat) -> BBox2D # keeps scale intact
        """
        Convert the format of 'bbox' of style 'XYXY'
        to 'target_format', without changing scale.
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
                output = XYXY_to_XmYmWH(bbox.value, pixel=True)
            elif target_format.style == "XcYcWH":
                output = XYXY_to_XcYcWH(bbox.value, pixel=True)
            elif target_format.style == "XYXY":
                output = bbox.value

        output_format = BBoxFormat(target_format.style, target_format.scale)
        return BBox2D(output, output_format)

    # helper for self.to_format()
    def _rescale(source_bbox: BBox2D, target_format: BBoxFormat, image_width=None, image_height=None) -> BBox2D:

        source_rel  = source_bbox.format.is_relative
        target_rel = target_format.is_relative

        # boolean * boolean = 4 possibilities

        if (source_rel and target_rel):
            scaled_bbox = BBox2D(
                xyxy_simple_rescale(
                    coords = source_bbox.value,
                    from_scale = source_bbox.format.scale,
                    to_scale = target.format.scale),
                source_bbox.format
                )
        elif (source_rel and (not target_rel)):
            _validate_image_size(image_width, image_height)
            scaled_bbox = BBox2D(
                xyxy_scaled_rel_to_abs(
                    coords = source_bbox.value,
                    from_scale = source_bbox.format.scale,
                    width = image_width,
                    height = image_height),
                source_bbox.format
            )
        elif ((not source_rel) and target_rel):
            _validate_image_size(image_width, image_height)
            scaled_bbox = BBox2D(
                xyxy_abs_to_scaled_rel(
                    coords = source_bbox.value,
                    to_scale = target.format.scale,
                    width = image_width,
                    height = image_height),
                source_bbox.format
            )
        else: # both absolute
            scaled_bbox = source_bbox

        return scaled_bbox

    # helper for self.to_format()
    def _xyxyify(bbox: BBox2D) -> BBox2D:
        """
        Convert 'bbox' style to 'XYXY'.
        Keep scale unchanged.
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
                output = XmYmWH_to_XYXY(bbox.value, pixel=True)
            elif bbox.format.style == "XcYcWH":
                output = XcYcWH_to_XYXY(bbox.value, pixel=True)
            elif bbox.format.style == "XYXY":
                output = bbox.value

        xyxy_format_same_scale = BBoxFormat("XYXY", bbox.format.scale) # only style was changed. Scale was not changed.

        return BBox2D(output, xyxy_format_same_scale)

    # helper for self.to_format()
    def _validate_image_size(image_width, image_height):
        if image_width is None or image_height is None:
            raise ValueError("Must enter 'image_width' and 'image_height' when converting across absolute and relative formats.")
        if image_width <= 0 or image_height <= 0:
            raise ValueError("Image width and height must be greater than zero.")

    # helper for self.__init__()
    def _validate_box(self, x):
        if isinstance(x, BBox2D):
            x = x.numpy(mode=mode)

        elif isinstance(x, (list, tuple)):
            if len(x) != 4:
                raise ValueError(
                    "Invalid input length. Input should have 4 elements.")
            x = np.asarray(x)

        elif isinstance(x, np.ndarray):
            if x.ndim >= 2:
                x = x.flatten()
            if x.size != 4:
                raise ValueError(
                    "Invalid input length. Input should have 4 elements.")
        else:
            raise TypeError(
                "Expected input to constructor to be a 4 element "
                "list, tuple, numpy ndarray, or BBox2D object.")
        return x


    # basic magic methods
    def __repr__(self):
        return f"BBox2D({self.value}, BBoxFormat({self.format.style}, {self.format.scale}))"

    def __str__(self):
        print(self.format.scale)
        return f"bbox: {self.value}, format style: {self.format.style}, format scale: {self.format.scale}"

    # Python magic methods

    def __eq__(self, other):
        """
        Strict equals.
        Bounding box value and format must both match.
        """
        raise NotImplementedError
    def __and__(self, other):
        """
        Return new bounding box that is the rectangular intersection between two given bounding boxes.
        """
        raise NotImplementedError
    def __or__(self, other):
        """
        Return new bounding box that contains the union of both bounding boxes tightly.
        """
        raise NotImplementedError
    def __round__(self):
        """
        Round values of bounding box to nearest integer.
        """
        raise NotImplementedError


    @property
    def format(self):
        return self._format

    @property
    def value(self):
        """
        Value of length 4 that represents bounding box.
        Order and meaning of values depend on format.
        """
        return self._value

    @property
    def x1(self):
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[0]
        else:
            raise AttributeError("x1 attribute not available for format: f{self.format}")

    @x1.setter
    def x1(self, value):
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[0] = value
        else:
            raise AttributeError("x1 attribute not available for format: f{self.format}")

    @property
    def x2(self):
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[2]
        else:
            raise AttributeError("x2 attribute not available for format: f{self.format}")

    @x2.setter
    def x2(self, value):
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[2] = value
        else:
            raise AttributeError("x1 attribute not available for format: f{self.format}")

    @property
    def xc(self):
        if self.format.style in ["XcYcWH"]:
            return self.value[0]
        else:
            raise AttributeError("x_center attribute not available for format: f{self.format}")

    @xc.setter
    def xc(self, value):
        if self.format.style in ["XcYcWH"]:
            self.value[0] = value
        else:
            raise AttributeError("x_center attribute not available for format: f{self.format}")

    @property
    def y1(self):
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[1]
        else:
            raise AttributeError("y1 attribute not available for format: f{self.format}")

    @y1.setter
    def y1(self, value):
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[1] = value
        else:
            raise AttributeError("y1 attribute not available for format: f{self.format}")

    @property
    def y2(self):
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[3]
        else:
            raise AttributeError("y2 attribute not available for format: f{self.format}")

    @y2.setter
    def y2(self, value):
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[3] = value
        else:
            raise AttributeError("y2 attribute not available for format: f{self.format}")

    @property
    def yc(self):
        if self.format.style in ["XcYcWH"]:
            return self.value[1]
        else:
            raise AttributeError("y_center attribute not available for format: f{self.format}")

    @yc.setter
    def yc(self, value):
        if self.format in ["XcYcWH"]:
            self.value[1] = value
        else:
            raise AttributeError("y_center attribute not available for format: f{self.format}")

    @property
    def w(self):
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            return self.value[2]
        else:
            raise AttributeError("width not available for format: f{self.format}")

    @w.setter
    def w(self, value):
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            self.value[2] = value
        else:
            raise AttributeError("width not available for format: f{self.format}")

    @property
    def h(self):
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            return self.value[3]
        else:
            raise AttributeError("height not available for format: f{self.format}")

    @h.setter
    def h(self, value):
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            self.value[3] = value
        else:
            raise AttributeError("height not available for format: f{self.format}")

    def yolo(self, image_width=None, image_height=None):
        if (self.format.is_relative != yolo.is_relative):
            # converting across relative/absolute scales
            _validate_image_size(image_width, image_height):
        return self.to_format(target_format=yolo, image_width, image_height)

if __name__ == "__main__":
    bbox = BBox2D([15,20,40,50], label_studio)
    print(bbox)
    print(bbox.format)
    print(bbox.format.style)
    print(bbox.value)
