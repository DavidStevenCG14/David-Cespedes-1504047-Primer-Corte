#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: hello_test.py
# Description: This program tests the module 'hello'
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import hello

class HelloTest(unittest.TestCase):
    def test_hello_noarg(self):
        self.assertEqual( 'Hello, World!', hello.salute() )
    def test_hello_none(self):
        self.assertEqual( 'Hello, World!', hello.salute(None) )
    def test_hello_empty(self):
        self.assertEqual( 'Hello, World!', hello.salute('') )
    def test_hello_name(self):
        self.assertEqual( 'Hello, Diego!', hello.salute('Diego') )

if __name__ == "__main__":
    unittest.main()

