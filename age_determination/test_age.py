# python -m unittest test_age -v

import unittest
from age import categorizeByAge

class ByAge(unittest.TestCase):
    def test_invalid(self):
        self.assertEqual(categorizeByAge(1000), "invalid age: 1000")
        self.assertEqual(categorizeByAge(1300), "invalid age: 1300")
    
    def test_child(self):
        self.assertEqual(categorizeByAge(6), "child")
    def test_teenager(self):
        self.assertEqual(categorizeByAge(14), "teenager")
    def test_adult(self):
        self.assertEqual(categorizeByAge(19), "adult")
    def test_goldenAge(self):
        self.assertEqual(categorizeByAge(66), "golden age")

    