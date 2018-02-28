import unittest
import numpy as np
from geolang.src.classifiers.bunch_data import get_catagories
from geolang.src.classifiers.bunch_data import bunch_training
import sys
import os

currpath = sys.path[0]
optimumpath = currpath[:-5] + "/geolang/src/classifiers"
os.chdir(optimumpath)

class TestBunchData(unittest.TestCase):
    def test_get_catagories(self):
        catagories = get_catagories()
        self.assertEqual("alabama", catagories[0])

    def test_bunch_training(self):
        trainingall = bunch_training(training_data='all')
        traininglex = bunch_training(training_data='lexicon')
        trainingsb = bunch_training(training_data='transcripts')
        self.assertEqual(58250, len(trainingall.target))
        self.assertEqual(36955, len(traininglex.target))
        self.assertEqual(21295, len(trainingsb.target))
        with self.assertRaises(ValueError):
            bunch_training(training_data='test')

suite = unittest.TestLoader().loadTestsFromTestCase(TestBunchData)
unittest.TextTestRunner(verbosity=2).run(suite)
