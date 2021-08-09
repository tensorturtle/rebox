from .bboxformat import BBoxFormat
# common research bounding box annotation formats
yolo = BBoxFormat(style='XcYcWH', scale=1)
coco = BBoxFormat(style='XmYmWH', scale=None)
pascal = BBoxFormat(style='XYXY', scale=None)
albumentations = BBoxFormat(style='XYXY', scale=1)
label_studio= BBoxFormat(style='XmYmWH', scale=100)
