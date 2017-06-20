#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: sequence_test.py
# Description: This program tests the module 'sequence'
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import sequence

class EvenTest(unittest.TestCase):
    def test_even_1(self):
        self.assertFalse( sequence.is_even(1) )
    def test_even_2(self):
        self.assertTrue( sequence.is_even(2) )
    def test_even_3(self):
        self.assertFalse( sequence.is_even(205) )
    def test_even_4(self):
        self.assertTrue( sequence.is_even(306) )
    def test_even_5(self):
        self.assertTrue( sequence.is_even(50) )

class OddTest(unittest.TestCase):
    def test_odd_1(self):
        self.assertTrue( sequence.is_odd(1) )
    def test_odd_2(self):
        self.assertFalse( sequence.is_odd(2) )
    def test_odd_3(self):
        self.assertTrue( sequence.is_odd(205) )
    def test_odd_4(self):
        self.assertFalse( sequence.is_odd(306) )
    def test_odd_5(self):
        self.assertFalse( sequence.is_odd(50) )

class SequenceTest(unittest.TestCase):
    def test_sequence_1(self):
        self.assertEqual( 17, sequence.sequence(15) )
    def test_sequence_2(self):
        self.assertEqual( 1, sequence.sequence(2) )
    def test_sequence_3(self):
        self.assertEqual( 118, sequence.sequence(97) )
    def test_sequence_4(self):
        self.assertEqual( 92, sequence.sequence(91) )
    def test_sequence_5(self):
        self.assertEqual( 17, sequence.sequence(602) )

if __name__ == "__main__":
    unittest.main()

