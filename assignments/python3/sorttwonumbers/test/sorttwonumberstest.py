import sys
import unittest
sys.path.append("..")
import sorttwonumbers  # noqa: E402


class Test(unittest.TestCase):
    def setUp(self):
        print('Running unittest on sorttwonumbers module')
        self.input1 = [5, 2]
        self.input2 = [-3, 10]
        self.input3 = [0, 0]

    def testSortNumbers1(self):
        expect = [2, 5]
        result = sorttwonumbers.sort_two_numbers(*self.input1)
        self.assertEqual(expect, result)

    def testSortNumbers2(self):
        expect = [-3, 10]
        result = sorttwonumbers.sort_two_numbers(*self.input2)
        self.assertEqual(expect, result)

    def testSortNumbers3(self):
        expect = [0, 0]
        result = sorttwonumbers.sort_two_numbers(*self.input3)
        self.assertEqual(expect, result)

    def tearDown(self):
        print('Done running unittest')


if __name__ == "__main__":
    unittest.main()
