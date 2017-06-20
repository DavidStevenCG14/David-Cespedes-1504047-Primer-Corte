#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: seconds_test.py
# Description: This program unittest the module seconds
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import seconds

class DaysBetweenTests(unittest.TestCase):
    def test_seconds_01(self):
        self.assertEqual( (2, 1, 10, 10, 5, 20), seconds.convert_seconds(66564320) )
    def test_seconds_02(self):
        self.assertEqual( (1, 6, 21, 16, 42, 14), seconds.convert_seconds(48962534) )
    def test_seconds_03(self):
        self.assertEqual( (0, 9, 16, 7, 15, 41), seconds.convert_seconds(24736541) )
    def test_seconds_04(self):
        self.assertEqual( (1, 0, 25, 6, 35, 53), seconds.convert_seconds(33719753) )
    def test_seconds_05(self):
        self.assertEqual( (0, 0, 23, 13, 8, 32), seconds.convert_seconds(2034512) )

if __name__ == "__main__":
    unittest.main()

