"""Main package initialization"""

from bboxconvert.bbox import BBox2D
from bboxconvert.format import BBoxFormat
from bboxconvert.common_formats import yolo, coco, pascal, albumentations, label_studio
from bboxconvert.converter import bboxconvert
from bboxconvert.elements import *


__author__ = "Jason Sohn"
__copyright__ = "Jason Sohn, 2021"
__version__ = "0.1.0"
__maintainer__ = "Jason Sohn"
__email__ = "tensorturtle@gmail.com"
__status__ = "Beta"
__license__ = "MIT"
