#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: sum_test.py
# Description: This program tests the module 'sum'
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import sum

class SumTest(unittest.TestCase):
    def test_sum_1(self):
        self.assertEqual( 50, sum.sum(3, 20, 5) )
    def test_sum_2(self):
        self.assertEqual( 55944, sum.sum(1, 1000, 9) )
    def test_sum_3(self):
        self.assertEqual( 325, sum.sum(1, 25, 1) )
    def test_sum_4(self):
        self.assertEqual( 539, sum.sum(10, 90, 7) )
    def test_sum_5(self):
        self.assertEqual( 16016, sum.sum(1000, 2000, 91) )

if __name__ == "__main__":
    unittest.main()

