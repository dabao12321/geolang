import unittest
import numpy as np
import pandas as pd
from geolang.src.cleaners.parse_SB_transcriptions import format_word
from geolang.src.cleaners.parse_SB_transcriptions import clean_line

class TestParseSBData(unittest.TestCase):
    def test_format_word(self):
        word = "he=l~lo"
        self.assertEqual("hello", format_word(word))

    def test_format_line(self):
        line = "... So you don't need to go ... borrow equipment from anybody,"
        self.assertListEqual(['you', "don't", 'need', 'to', 'go', 'borrow', 'equipment', 'from', 'anybody'], clean_line(line))

suite = unittest.TestLoader().loadTestsFromTestCase(TestParseSBData)
unittest.TextTestRunner(verbosity=2).run(suite)
