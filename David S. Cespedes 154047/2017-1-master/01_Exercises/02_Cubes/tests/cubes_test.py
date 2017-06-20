#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: cubes_test.py
# Description: This program unittest the module cubes
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import cubes

class CubesTests(unittest.TestCase):
    def test_cubes_01(self):
        self.assertEqual( 36, cubes.cubes(1, 3) )
    def test_cubes_02(self):
        self.assertEqual( 784, cubes.cubes(1, 7) )
    def test_cubes_03(self):
        self.assertEqual( 4788, cubes.cubes(9, 12) )
    def test_cubes_04(self):
        self.assertEqual( 20384, cubes.cubes(11, 17) )
    def test_cubes_05(self):
        self.assertEqual( 32076, cubes.cubes(21, 23) )

if __name__ == "__main__":
    unittest.main()

