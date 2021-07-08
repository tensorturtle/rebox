import unittest

from bboxconvert.bboxconvert import * 
from bboxconvert.elements import *

class BboxTest(unittest.TestCase):
    def test_coordinate_conversions(self):
        data = [1,1,1,1]
        result = coco_to_voc(data)
        self.asserEqual(result, [1,1,2,2])

if __name__=='__main__':
    unittest.main()
