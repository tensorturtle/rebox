# bboxconvert
Minimal library to convert between unrotated rectangular bounding box annotation formats.

## Common Bounding Box Format Specifications



## Shortcut Conversions Between Popular Dataset Formats

| from (column) to (row) 	| YOLO           	| COCO           	| PASCAL_VOC    	| Albumentations 	|
|------------------------:|:---------------:|:---------------:|:--------------: |:---------------:|
| YOLO                  	| 🌸              	| yolo_to_coco() 	| yolo_to_voc() 	| yolo_to_A      	|
| COCO                   	| coco_to_yolo() 	| 🌸              	| coco_to_voc() 	| coco_to_A      	|
| PASCAL_VOC            	| voc_to_yolo()  	| voc_to_coco()  	| 🌸             	| voc_to_A()     	|
| Albumentations         	| A_to_yolo()    	| A_to_coco()    	| A_to_voc()    	| 🌸              	|
