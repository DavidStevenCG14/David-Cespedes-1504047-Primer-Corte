#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: odd_even_test.py
# Description: This program unittest the module odd_even
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import odd_even

class OddEvenTests(unittest.TestCase):
    def test_odd_even_01(self):
        self.assertEqual( ([], []), odd_even.odd_even([]) )
    def test_odd_even_02(self):
        self.assertEqual( ([], [2, 4, 6, 8]), odd_even.odd_even([2, 4, 6, 8]) )
    def test_odd_even_03(self):
        self.assertEqual( ([1, 3, 5, 7, 9], []), odd_even.odd_even([1, 3, 5, 7, 9]) )
    def test_odd_even_04(self):
        self.assertEqual( ([7], [20]), odd_even.odd_even([7, 20]) )
    def test_odd_even_05(self):
        self.assertEqual( ([1, 3, 5, 7, 9], [2, 4, 6, 8]), odd_even.odd_even([1, 2, 3, 4, 5, 6, 7, 8, 9]) )

if __name__ == "__main__":
    unittest.main()

