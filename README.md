# bboxconvert
Minimal library to convert between bounding box annotation formats.

## Popular Dataset Formats

| from (down this column)  to (across this row) 	| YOLO           	| COCO           	| PASCAL_VOC    	| Albumentations 	|
|:-----------------------------------------------:|:---------------:|:---------------:|:--------------: |:---------------:|
| YOLO                                          	| X              	| yolo_to_coco() 	| yolo_to_voc() 	| yolo_to_A      	|
| COCO                                          	| coco_to_yolo() 	| X              	| coco_to_voc() 	| coco_to_A      	|
| PASCAL_VOC                                    	| voc_to_yolo()  	| voc_to_coco()  	| X             	| voc_to_A()     	|
| Albumentations                                	| A_to_yolo()    	| A_to_coco()    	| A_to_voc()    	| X              	|
