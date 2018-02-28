import unittest
import numpy as np
from geolang.src.classifiers.naive_bayes import predict_multinomial_NB
import sys
import os

currpath = sys.path[0]
optimumpath = currpath[:-5] + "/geolang/src/classifiers"
os.chdir(optimumpath)

class TestNaiveBayes(unittest.TestCase):
    def test_predict_multinomial_NB(self):
        testing = ['What a gooselock!',
            'Scoot your tush over.',
            "That's a hosey. Don't barf up your frappe.",
            "gosh hm Leah She snoozing on the floor"]
        self.assertListEqual(['alabama', 'virginia', 'massachusetts', 'oklahoma'], predict_multinomial_NB(testing))

suite = unittest.TestLoader().loadTestsFromTestCase(TestNaiveBayes)
unittest.TextTestRunner(verbosity=2).run(suite)
