#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: add_days_test.py
# Description: This program unittest the module add_days
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import add_days

class AddDaysTests(unittest.TestCase):
    def test_add_days_01(self):
        self.assertEqual( '2017-02-10', add_days.add_days('2017-01-01', 40) )
    def test_add_days_02(self):
        self.assertEqual( '2016-05-15', add_days.add_days('2015-01-01', 500) )
    def test_add_days_03(self):
        self.assertEqual( '2017-07-10', add_days.add_days('2013-06-04', 1497) )
    def test_add_days_04(self):
        self.assertEqual( '2017-02-28', add_days.add_days('2016-09-01', 180) )
    def test_add_days_05(self):
        self.assertEqual( '2017-03-18', add_days.add_days('2000-01-01', 6286) )

if __name__ == "__main__":
    unittest.main()

