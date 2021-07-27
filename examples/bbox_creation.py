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

