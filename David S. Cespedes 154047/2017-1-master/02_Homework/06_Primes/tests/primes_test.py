#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: primes_test.py
# Description: This program unittest the module primes
# Author: juan cano vasquez

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import primes

class PrimesTests(unittest.TestCase):
    def test_primes_01(self):
        self.assertEqual( ([22], [17, 19]), primes.primees([17, 19, 22]) )
    def test_primes_02(self):
        self.assertEqual( ([4, 6, 8], [2]), primes.primees([2, 4, 6, 8]) )
    def test_primes_03(self):
        self.assertEqual( ([1, 9], [3, 5, 7]), primes.primees([1, 3, 5, 7, 9]) )
    def test_primes_03(self):
        self.assertEqual( ([20], [7]), primes.primees([7, 20]) )
    def test_primes_05(self):
        self.assertEqual( ([9, 10], [11, 13]), primes.primees([9, 10, 11, 13]) )

if __name__ == "__main__":
    unittest.main()