class BBoxFormat:

    """
    Class from which bounding box formats are generated.
    The built-in common formats are created with this class.
    Feel free to create your own from this class.

    Attributes:
        style = one of 3 ways to represent a rectangular box XmYmWH (left-top corner, width, and height), XcYcWH (center point, width and height), or XYXY (left-top corner, and bottom-right corner)
        scale = None for pixel value, or integer for range of normalized value (relative to image width or height)
        is_relative = syntactic sugar; boolean False if scale is None, and True if it is a number.


    Raises:
        ValueError: If scale is negative

    Example:
        COCO_format = BBoxFormat(style='XmYmWH', scale='none')
        YOLO_format = BBoxFormat(style='XcYcWH', scale='1')
    """

    def __init__(self, style, scale):

        """
        Args:
            style = choose from 3 ways to represent a rectangular box XmYmWH (left-top corner, width, and height), XcYcWH (center point, width and height), or XYXY (left-top corner, and bottom-right corner)
            scale = If using pixel coordinates, enter None. Otherwise, enter maximum value of scale (for example, 100 for scaling to between 0 and 100, like percent)
        """
        valid_styles = ["XmYmWH, XcYcWH, XYXY"] # currently 3 supported styles
        try:
            style in valid_styles
        except ValueError as err:
            print("Style is unrecognized. Choose among: 'XmYmWH, 'XcYcWH', or 'XYXY'", err)
        self._style = style

        if scale == None:
            self._scale = None
        else:
            try:
                scale > 0
            except ValueError as err:
                print("Scale cannot be negative.", err)
            self._scale = int(scale)

        self._is_relative = (scale is not None)

    @property
    def style(self):
        """
        What do the four numbers in an annotation signify?
        """
        return self._style

    @property
    def scale(self):
        """
        What, if any, normalization or scaling has been applied to the location information of the bounding box?
        """
        return self._scale

    @property
    def is_relative(self):
        """
        Has this bounding box annotation been scaled relative to image height and width?
        Syntactic sugar for determining if image width and height information are required for converting to absolute-scale coordinates.
        """
        return (self._scale is not None)

if __name__ == "__main__":
    label_studio_format = BBoxFormat(style='XmYmWH', scale=100)
    print(label_studio_format.style)
    print(label_studio_format.scale)
    print(label_studio_format.is_relative)
