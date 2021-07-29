import numpy as np

def XcYcWH_to_XYXY(coords):
    '''
    [x_center, y_center, width, height]
    to
    [x_min, y_min, x_max, y_max]
    '''
    x_center = coords[0]
    y_center = coords[1]
    width = coords[2]
    height = coords[3]

    x_min = x_center - (width/2)
    y_min = y_center - (height/2)
    x_max = x_center + (width/2)
    y_max = y_center + (height/2)

    return np.around(np.array([x_min, y_min, x_max, y_max]), decimals=4)

def XYXY_to_XcYcWH(coords):
    '''
    [x_min, y_min, x_max, y_max]
    to
    [x_center, y_center, width, height]
    '''
    x_min = coords[0]
    y_min = coords[1]
    x_max = coords[2]
    y_max = coords[3]

    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    width = x_max - x_min
    height = y_max - y_min

    return np.around(np.array([x_center, y_center, width, height]), decimals=4)

def XmYmWH_to_XYXY(coords):
    x_min = coords[0]
    y_min = coords[1]
    width = coords[2]
    height = coords[3]

    x_max = x_min + width
    y_max = y_min + height

    return np.around(np.array([x_min, y_min, x_max, y_max]), decimals=4)

def XYXY_to_XmYmWH(coords):
    x_min = coords[0]
    y_min = coords[1]
    x_max = coords[2]
    y_max = coords[3]

    width = x_max - x_min
    height = y_max - y_min

    return np.around(np.array([x_min, y_min, width, height]), decimals=4)

def normalize(coords, width, height):
    '''
    Normalize pixel values to [0,1]
    Assuming [x,y,x,y] values
    '''
    return np.around(np.array([coords[0]/width, coords[1]/height, coords[2]/width, coords[3]/height]), decimals=4)

def denormalize(coords, width, height):
    '''
    Expand normalized values to full pixel range
    Assuming [x,y,x,y] values
    '''
    return np.around(np.array([coords[0]*width, coords[1]*height, coords[2]*width, coords[3]*height]), decimals=4)

def xyxy_scaled_rel_to_abs(coords, from_scale, width, height):
    x_min = coords[0]
    y_min = coords[1]
    x_max = coords[2]
    y_max = coords[3]

    abs_x_min = x_min / from_scale * width
    abs_y_min = y_min / from_scale * height
    abs_x_max = x_max / from_scale * width
    abs_y_max = y_max / from_scale * height

    return np.around(np.array([abs_x_min, abs_y_min, abs_x_max, abs_y_max]), decimals=4)

def xyxy_abs_to_scaled_rel(coords, to_scale, width, height):
    abs_x_min = coords[0]
    abs_y_min = coords[1]
    abs_x_max = coords[2]
    abs_y_max = coords[3]

    rel_x_min = abs_x_min / width
    rel_y_min = abs_y_min / height
    rel_x_max = abs_x_max / width
    rel_y_max = abs_y_max / height

    x_min = rel_x_min * to_scale
    y_min = rel_y_min * to_scale
    x_max = rel_x_max * to_scale
    y_max = rel_y_max * to_scale

    return np.array([x_min, y_min, x_max, y_max])

def xyxy_simple_rescale(coords, from_scale, to_scale):
    return np.around(np.array(coords / from_scale * to_scale), decimals=4)
