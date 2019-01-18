import unittest


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_open_browser(self):
        assert False
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    if __name__ == '__main__':
        unittest.main()