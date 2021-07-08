import unittest

from bboxconvert import test_sum
from bboxconvert.bboxconvert import coco_to_voc

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3]
        result = test_sum(data)
        self.assertEqual(result, 6)

class BboxTest(unittest.TestCase):
    def test_coordinate_conversions(self):
        data = [1,1,1,1]
        result = coco_to_voc(data)
        self.asserEqual(result, [1,1,2,2])

if __name__=='__main__':
    unittest.main()
