import unittest
import numpy as np
import pandas as pd
from geolang.src.cleaners.parse_dare_corpus import expand_region

class TestParseDareCorpus(unittest.TestCase):
    def test_expand_region(self):
        test = pd.DataFrame({'dialect':['washington', 'oregon', 'california'], 'word': ['test', 'test', 'test']})
        output = expand_region('pacific', 'test')
        self.assertListEqual(pd.Series.tolist(test['dialect']), pd.Series.tolist(output['dialect']))
        self.assertListEqual(pd.Series.tolist(test['word']), pd.Series.tolist(output['word']))

suite = unittest.TestLoader().loadTestsFromTestCase(TestParseDareCorpus)
unittest.TextTestRunner(verbosity=2).run(suite)
