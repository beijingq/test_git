import unittest

class Test(unittest.TestCase):
    # def setUp(self):
    #     print("setup")
    # def tearDown(self):
    #     print("teadown")
    def setUpClass(self):
        print("setup")
    def tearDownClass(self):
        print("teadown")
    def test_1(self):
        print("test1")

    def test_2(self):
        print("test2")