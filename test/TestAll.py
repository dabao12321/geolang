import unittest
from TestBunchData import TestBunchData
from TestCleanGeodata import TestCleanGeodata
from TestNaiveBayes import TestNaiveBayes
from TestParseDareCorpus import TestParseDareCorpus
from TestParseSBData import TestParseSBData
from TestVectorizeData import TestVectorizeData

def suite():
    """
        Gather all the tests from this directory in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestBunchData))
    test_suite.addTest(unittest.makeSuite(TestCleanGeodata))
    test_suite.addTest(unittest.makeSuite(TestNaiveBayes))
    test_suite.addTest(unittest.makeSuite(TestParseDareCorpus))
    test_suite.addTest(unittest.makeSuite(TestParseSBData))
    test_suite.addTest(unittest.makeSuite(TestVectorizeData))
    return test_suite

mySuit=suite()
runner=unittest.TextTestRunner()
runner.run(mySuit)
