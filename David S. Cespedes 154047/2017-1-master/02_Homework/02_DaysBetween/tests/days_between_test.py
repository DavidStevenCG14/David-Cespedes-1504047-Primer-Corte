#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: days_between_test.py
# Description: This program unittest the module days_between
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import days_between

class DaysBetweenTests(unittest.TestCase):
    def test_days_between_01(self):
        self.assertEqual( 40, days_between.days_between('2017-01-01', '2017-02-10') )
    def test_days_between_02(self):
        self.assertEqual( 500, days_between.days_between('2015-01-01', '2016-05-15') )
    def test_days_between_03(self):
        self.assertEqual( 1947, days_between.days_between('2013-06-04', '2017-07-10') )
    def test_days_between_04(self):
        self.assertEqual( 180, days_between.days_between('2016-09-01', '2017-02-28') )
    def test_days_between_05(self):
        self.assertEqual( 6286, days_between.days_between('2000-01-01', '2017-03-18') )

if __name__ == "__main__":
    unittest.main()

