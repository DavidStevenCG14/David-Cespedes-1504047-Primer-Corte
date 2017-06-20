#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: count_test.py
# Description: This program tests the module 'count'
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import count

class CountTest(unittest.TestCase):
    def test_count_1(self):
        self.assertEqual( 4, count.count(3, 20, 5) )
    def test_count_2(self):
        self.assertEqual( 111, count.count(1, 1000, 9) )
    def test_count_3(self):
        self.assertEqual( 25, count.count(1, 25, 1) )
    def test_count_4(self):
        self.assertEqual( 11, count.count(10, 90, 7) )
    def test_count_5(self):
        self.assertEqual( 11, count.count(1000, 2000, 91) )

if __name__ == "__main__":
    unittest.main()

