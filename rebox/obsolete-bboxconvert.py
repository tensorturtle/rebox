from .elements import *

def yolo_to_coco(c,w,h):
    return denormalize(xyXY_to_xywh(xCyCwh_to_xyXY(c)),w,h)

def yolo_to_voc(c,w,h):
    return denormalize(xCyCwh_to_xyXY(c),w,h)

def yolo_to_A(c):
    return xCyCwh_to_xyXY(c)

def coco_to_yolo(c,w,h):
    return normalize(xyXY_to_xCyCwh(xywh_to_xyXY(c)),w,h)

def coco_to_voc(c):
    return xywh_to_xyXY(c)

def coco_to_A(c,w,h):
    return normalize(xywh_to_xyXY(c),w,h)

def voc_to_yolo(c,w,h):
    return normalize(xyXY_to_xCyCwh(c),w,h)

def voc_to_coco(c):
    return xyXY_to_xywh(c)

def voc_to_A(c,w,h):
    return normalize(c,w,h)

def A_to_yolo(c):
    return xyXY_to_xCyCwh(c)

def A_to_coco(c,w,h):
    return denormalize(xyXY_to_xywh(c),w,h)

def A_to_voc(c,w,h):
    return denormalize(c,w,h)


if __name__=='__main__':
    pass
