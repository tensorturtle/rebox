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
    x_max = y_center + (height/2)

    return [x_min, y_min, x_max, y_max]

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

    return [x_center, y_center, width, height]

def XmYmWH_to_XYXY(coords):
    x_min = coords[0]
    y_min = coords[1]
    width = coords[2]
    height = coords[3]

    x_max = x_min + width
    y_max = y_min + height

    return [x_min, y_min, x_max, y_max]

def XYXY_to_XmYmWH(coords):
    x_min = coords[0]
    y_min = coords[1]
    x_max = coords[2]
    y_max = coords[3]

    width = x_max - x_min
    height = y_max - y_min

    return [x_min, y_min, width, height]

def normalize(coords, width, height):
    '''
    Normalize pixel values to [0,1]
    Assuming [x,y,x,y] values
    '''
    return [coords[0]/width, coords[1]/height, coords[2]/width, coords[3]/height]

def denormalize(coords, width, height):
    '''
    Expand normalized values to full pixel range
    Assuming [x,y,x,y] values
    '''
    return [coords[0]*width, coords[1]*height, coords[2]*width, coords[3]*height]

def pixel_XmYmWH_to_XYXY(coords):
    x_min = coords[0]
    y_min = coords[1]
    width = coords[2]
    height = coords[3]

    x_max = x_min + width - 1 # accounting for fencepost error; pixel bounding box width/height is taken to be the 'outside' measure
    y_max = y_min + height - 1
    return [x_min, y_min, x_max, y_max]

def pixel_XcYcWH_to_XYXY(coords):
    x_center = coords[0]
    y_center = coords[1]
    width = coords[2]
    height = coords[3]

    exact_width = width - 1 # accounting for fencepost error; pixel bounding box width/height is taken to be the 'outside' measure
    exact_height = height - 1

    x_min = x_center - exact_width/2
    x_max = x_center + exact_width/2
    y_min = y_center - exact_height/2
    y_max = y_center + exact_height/2

    return [x_min, y_min, x_max, y_max]

def pixel_XYXY_to_XmYmWH(coords):
    x_min = coords[0]
    y_min = coords[1]
    x_max = coords[2]
    y_max = coords[3]

    exact_width = x_max - x_min
    fencepost_width = exact_width + 1

    exact_height = y_max - y_min
    fencepost_height = exact_height + 1

    return [x_min, y_min, fencepost_width, fencepost_height]

def pixel_XYXY_to_XcYcWH(coords):
    x_min = coords[0]
    y_min = coords[1]
    x_max = coords[2]
    y_max = coords[3]

    x_center = (x_max - x_min) / 2
    y_center = (y_max - y_min) / 2

    exact_width = x_max - x_min
    fencepost_width = exact_width + 1

    exact_height = y_max - y_min
    fencepost_height = exact_height + 1

    return [x_center, y_center, fencepost_width, fencepost_height]

def xyxy_scaled_rel_to_abs(coords, scale, width, height):
    x_min = coords[0]
    y_min = coords[1]
    x_max = coords[2]
    y_max = coords[3]

    abs_x_min = x_min / scale * width
    abs_y_min = y_min / scale * height
    abs_x_max = x_max / scale * width
    abs_y_max = y_max / scale * height

    return [abs_x_min, abs_y_min, abs_x_max, abs_y_max]

def xyxy_abs_to_scaled_rel(coords, scale, width, height):
    abs_x_min = coords[0]
    abs_y_min = coords[1]
    abs_x_max = coords[2]
    abs_y_max = coords[3]

    rel_x_min = abs_x_min / width
    rel_y_min = abs_y_min / height
    rel_x_max = abs_x_max / width
    rel_y_max = abs_y_max / height

    x_min = rel_x_min * scale
    y_min = rel_y_min * scale
    x_max = rel_x_max * scale
    y_max = rel_y_max * scale

    return [x_min, y_min, x_max, y_max]
