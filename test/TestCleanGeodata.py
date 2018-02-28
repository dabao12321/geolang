import unittest
import numpy as np
from geolang.src.cleaners.clean_geodata import abbrev_to_state

class TestCleanGeodata(unittest.TestCase):
    def test_abbrev_to_state(self):
        self.assertEqual("massachusetts", abbrev_to_state("ma"))
        self.assertEqual("massachusetts, maine", abbrev_to_state("ma, me"))
        with self.assertRaises(ValueError):
            abbrev_to_state("n/a")

suite = unittest.TestLoader().loadTestsFromTestCase(TestCleanGeodata)
unittest.TextTestRunner(verbosity=2).run(suite)
