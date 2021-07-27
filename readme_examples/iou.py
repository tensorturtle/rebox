from rebox import BBox
from rebox.formats import coco, pascal
from rebox.ops import iou

one_bbox = BBox([40,50,20,10], coco)
two_bbox = BBox([45,60, 30, 20], pascal)

iou = iou(one_bbox, two_bbox)
