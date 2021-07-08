def xCyCwh_to_xyXY(coords):
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

def xyXY_to_xCyCwh(coords):
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

def xywh_to_xyXY(coords):
    x_min = coords[0]
    y_min = coords[1]
    width = coords[2]
    height = coords[3]

    x_max = x_min + width
    y_max = y_min + height

    return [x_min, y_min, x_max, y_max]

def xyXY_to_xywh(coords):
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
    

