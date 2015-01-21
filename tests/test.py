__author__ = 'nwilson'

import unittest

class MyTestCase(unittest.TestCase):

    @unittest.skip("this test is silly")
    def test_something(self):
        self.assertEqual(True, False)

    def test_somethingElse(self):
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()
