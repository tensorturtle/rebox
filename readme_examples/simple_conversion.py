from rebox import BBox
from rebox.formats import coco, pascal

coco_bbox = BBox([40,50,20,15], coco)
pascal_bbox = coco_bbox.as_format(pascal)

print(pascal_bbox) # "Coordinates: [40 50 59 64], Style: XYXY, Scale: None"
print(pascal_bbox.value) # [40 50 59 64]
