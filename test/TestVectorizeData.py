import unittest
import numpy as np
from geolang.src.classifiers.vectorize_data import get_shape
import sys
import os

currpath = sys.path[0]
optimumpath = currpath[:-5] + "/geolang/src/classifiers"
os.chdir(optimumpath)

class TestVectorizeData(unittest.TestCase):
    def test_get_shape(self):
        arr = [[1,0], [2, 3], [1, 1]]
        self.assertEqual((3, 2), get_shape(arr))

suite = unittest.TestLoader().loadTestsFromTestCase(TestVectorizeData)
unittest.TextTestRunner(verbosity=2).run(suite)
