"""2D bounding box module."""

from copy import deepcopy
import numpy as np

from .bboxformat import BBoxFormat
from .formats import yolo, coco, pascal, albumentations, label_studio
from .elements import XcYcWH_to_XYXY, XYXY_to_XcYcWH, XmYmWH_to_XYXY, XYXY_to_XmYmWH, xyxy_scaled_rel_to_abs, xyxy_abs_to_scaled_rel, xyxy_simple_rescale

class BBox:

    """
    Class to represent a 2D bounding box.

    Args:
        x: Sequence of length 4 representing bounding box coordinates.
        format: :py:class:BBoxFormat corresponding to format of x

    Raises:
        ValueError: If 'box' is not of length 4
        TypeError: If 'box' is not of type {list, tuple, numpy.ndarray, BBox
    """

    def __init__(self, x, bbox_format:BBoxFormat):
        x = self._validate_box(x)
        self._format = bbox_format
        self._value = x

    def as_format(self, target_format: BBoxFormat, image_width=None, image_height=None):
        # converting directly between all available formats means combinatorial numbers of operations. Therefore, to simply conversion, we convert 'self' to an interim 'XYXY' style, then apply scale, then convert interim style to target style
        interim = self._xyxyify(self)
        scaled_interim = self._rescale(interim, target_format, image_width, image_height)
        target_bbox = self._restyle(scaled_interim, target_format)
        return target_bbox

    # helper for self.to_format()
    @staticmethod
    def _restyle(bbox, target_format: BBoxFormat): # keeps scale intact
        """
        Convert the format of 'bbox' of style 'XYXY'
        to 'target_format', without changing scale.
        """
        if target_format.style == "XmYmWH":
            output = XYXY_to_XmYmWH(bbox.value)
        elif target_format.style == "XcYcWH":
            output = XYXY_to_XcYcWH(bbox.value)
        elif target_format.style == "XYXY":
            output = bbox.value
        else:
            raise AttributeError("target format is invalid")

        output_format = BBoxFormat(target_format.style, target_format.scale)
        return BBox(output, output_format)

    # helper for self.to_format()
    def _rescale(self, source_bbox, target_format: BBoxFormat, image_width=None, image_height=None):

        source_rel  = source_bbox.format.is_relative
        target_rel = target_format.is_relative

        # boolean * boolean = 4 possibilities

        if (source_rel and target_rel):
            scaled_bbox = BBox(
                xyxy_simple_rescale(
                    coords = source_bbox.value,
                    from_scale = source_bbox.format.scale,
                    to_scale = target_format.scale),
                source_bbox.format
                )
        elif (source_rel and (not target_rel)):
            self._validate_image_size(image_width, image_height)
            scaled_bbox = BBox(
                xyxy_scaled_rel_to_abs(
                    coords = source_bbox.value,
                    from_scale = source_bbox.format.scale,
                    width = image_width,
                    height = image_height),
                source_bbox.format
            )
        elif ((not source_rel) and target_rel):
            self._validate_image_size(image_width, image_height)
            scaled_bbox = BBox(
                xyxy_abs_to_scaled_rel(
                    coords = source_bbox.value,
                    to_scale = target_format.scale,
                    width = image_width,
                    height = image_height),
                source_bbox.format
            )
        else: # both absolute
            scaled_bbox = source_bbox

        return scaled_bbox

    # helper for self.to_format()
    @staticmethod
    def _xyxyify(bbox):
        """
        Convert 'bbox' style to 'XYXY'.
        Keep scale unchanged.
        """
        if bbox.format.style == "XmYmWH":
            output = XmYmWH_to_XYXY(bbox.value)
        elif bbox.format.style == "XcYcWH":
            output = XcYcWH_to_XYXY(bbox.value)
        elif bbox.format.style == "XYXY":
            output = bbox.value
        else:
            raise ValueError("Invalid format style given. Check format of bounding box.")

        xyxy_format_same_scale = BBoxFormat("XYXY", bbox.format.scale) # only style was changed. Scale was not changed.

        return BBox(output, xyxy_format_same_scale)

    # helper for self.to_format()
    @staticmethod
    def _validate_image_size(image_width, image_height):
        if image_width is None or image_height is None:
            raise ValueError("Must enter 'image_width' and 'image_height' when converting across absolute and relative formats.")
        if image_width <= 0 or image_height <= 0:
            raise ValueError("Image width and height must be greater than zero.")

    # helper for self.__init__()
    @staticmethod
    def _validate_box(x):
        if isinstance(x, BBox):
            x = x

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
                "list, tuple, numpy ndarray, or BBox object.")
        return x


    # basic magic methods
    def __repr__(self):
        return f"BBox({self.value}, BBoxFormat({self.format.style}, {self.format.scale}))"

    def __str__(self):
        print(self.format.scale)
        return f"Coordinates: {self.value}, Style: {self.format.style}, Scale: {self.format.scale}"

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
        Return numpy ndarray of length 4
        representing the coordinates of bounding box,
        formatted as `self.format`.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Set coordinates of bounding box
        """
        setting_value = np.array(value)
        if len(setting_value) != 4:
            raise ValueError("Input value is not of length 4")
        self._value = setting_value

    @property
    def x1(self):
        """
        get x value of left-top corner of bounding box
        """
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[0]
        else:
            raise AttributeError(f"x1 attribute not available for format: {self.format.style}")

    @x1.setter
    def x1(self, value):
        """
        set x value of left-top corner of bounding box
        """
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[0] = value
        else:
            raise AttributeError(f"x1 attribute not available for format: {self.format.style}")

    @property
    def x2(self):
        """
        get x value of right-bottom corner of bounding box
        """
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY"]:
            return self.value[2]
        else:
            raise AttributeError(f"x2 attribute not available for format: {self.format.style}")

    @x2.setter
    def x2(self, value):
        """
        set x value of right-bottom corner of bounding box
        """
        # if xyxy, XmYmWH
        if self.format.style in ["XYXY"]:
            self.value[2] = value
        else:
            raise AttributeError(f"x2 attribute not available for format: {self.format.style}")

    @property
    def xc(self):
        """
        get x value of center point of bounding box
        """
        if self.format.style in ["XcYcWH"]:
            return self.value[0]
        else:
            raise AttributeError(f"x_center attribute not available for format: {self.format.style}")

    @xc.setter
    def xc(self, value):
        """
        set x value of center point of bounding box
        """
        if self.format.style in ["XcYcWH"]:
            self.value[0] = value
        else:
            raise AttributeError(f"x_center attribute not available for format: {self.format.style}")

    @property
    def y1(self):
        """
        get y value of left-top corner of bounding box
        """
        if self.format.style in ["XYXY", "XmYmWH"]:
            return self.value[1]
        else:
            raise AttributeError(f"y1 attribute not available for format: {self.format.style}")

    @y1.setter
    def y1(self, value):
        """
        set y value of left-top corner of bounding box
        """
        if self.format.style in ["XYXY", "XmYmWH"]:
            self.value[1] = value
        else:
            raise AttributeError(f"y1 attribute not available for format: {self.format.style}")

    @property
    def y2(self):
        """
        get y value of right-bottom corner of bounding box
        """
        if self.format.style in ["XYXY"]:
            return self.value[3]
        else:
            raise AttributeError(f"y2 attribute not available for format: {self.format.style}")

    @y2.setter
    def y2(self, value):
        """
        set y value of right-bottom corner of bounding box
        """
        if self.format.style in ["XYXY"]:
            self.value[3] = value
        else:
            raise AttributeError(f"y2 attribute not available for format: {self.format.style}")

    @property
    def yc(self):
        """
        get y value of center point of bounding box
        """
        if self.format.style in ["XcYcWH"]:
            return self.value[1]
        else:
            raise AttributeError(f"y_center attribute not available for format: {self.format.style}")

    @yc.setter
    def yc(self, value):
        """
        set y value of center point of bounding box
        """
        if self.format in ["XcYcWH"]:
            self.value[1] = value
        else:
            raise AttributeError(f"y_center attribute not available for format: {self.format.style}")

    @property
    def w(self):
        """
        get width of bounding box
        """
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            return self.value[2]
        else:
            raise AttributeError(f"width not available for format: {self.format.style}")

    @w.setter
    def w(self, value):
        """
        set width of bounding box
        """
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            self.value[2] = value
        else:
            raise AttributeError(f"width not available for format: {self.format.style}")

    @property
    def h(self):
        """
        get height of bounding box
        """
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            return self.value[3]
        else:
            raise AttributeError(f"height not available for format: {self.format.style}")

    @h.setter
    def h(self, value):
        """
        set height of bounding box
        """
        if self.format.style in ["XcYcWH", "XmYmWH"]:
            self.value[3] = value
        else:
            raise AttributeError(f"height not available for format: {self.format.style}")

if __name__ == "__main__":
    bbox = BBox([15,20,40,50], label_studio)
    print(bbox)
    print(bbox.format)
    print(bbox.format.style)
    print(bbox.value)
