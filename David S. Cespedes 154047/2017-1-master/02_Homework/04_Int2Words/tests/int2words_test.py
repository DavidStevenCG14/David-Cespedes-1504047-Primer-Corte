#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: int2words_test.py
# Description: This program unittest the module int2words
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import int2words

class AddDaysTests(unittest.TestCase):
    def test_int2words_01(self):
        self.assertEqual( 'cuarenta y tres', int2words.int2words(43) )
    def test_int2words_02(self):
        self.assertEqual( 'doscientos diecisiete', int2words.int2words(217) )
    def test_int2words_03(self):
        self.assertEqual( 'tres mil ochocientos once', int2words.int2words(3811) )
    def test_int2words_04(self):
        self.assertEqual( 'cincuenta mil novecientos uno', int2words.int2words(50901) )
    def test_int2words_05(self):
        self.assertEqual( 'setecientos tres mil quinientos cuarenta y dos', int2words.int2words(703542) )

if __name__ == "__main__":
    unittest.main()

