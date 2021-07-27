from rebox import BBox
from rebox.formats import yolo, coco

image_height = 360 # pixels
image_width = 640 # pixels

yolo_bbox = BBox([0.31, 0.5, 0.2, 0.6], yolo) # using built-in 'yolo_format'

coco_bbox = yolo_bbox.as_format(coco, image_width, image_height) # to convert to built-in format 'coco'

print(coco_bbox.value) # array([134.4,  72. , 128. , 216. ])
