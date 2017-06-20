#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: hypotenuse_test.py
# Description: This program unittest the module hypotenuse
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import hypotenuse

class HypoTests(unittest.TestCase):
    def test_hypo_01(self):
        self.assertEqual( 5.0, hypotenuse.hypotenuse(3, 4) )
    def test_hypo_02(self):
        self.assertEqual( 5.0, hypotenuse.hypotenuse(4, 3) )
    def test_hypo_03(self):
        self.assertEqual( 22.847319317591726, hypotenuse.hypotenuse(9, 21) )
    def test_hypo_04(self):
        self.assertEqual( 20.248456731316587, hypotenuse.hypotenuse(17, 11) )
    def test_hypo_05(self):
        self.assertEqual( 403.8873605350878, hypotenuse.hypotenuse(210, 345) )

if __name__ == "__main__":
    unittest.main()

