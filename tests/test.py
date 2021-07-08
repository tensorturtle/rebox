import unittest

from bboxconvert import test_sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3]
        result = test_sum(data)
        self.assertEqual(result, 6)

if __name__=='__main__':
    unittest.main()
