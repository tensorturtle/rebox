from rebox import BBox
from rebox.formats coco, pascal
from rebox.ops import IOU

one_bbox = BBox([40,50,20,10], coco)
two_bbox = BBox([45,60, 30, 20], pascal)

iou = IOU(one_bbox, two_bbox)
