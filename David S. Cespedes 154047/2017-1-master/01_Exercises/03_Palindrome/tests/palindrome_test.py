#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: palindrome_test.py
# Description: This program unittest the module palindrome
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import palindrome

class PalindromeTests(unittest.TestCase):
    def test_palindrome_01(self):
        self.assertTrue( palindrome.palindrome("") )
    def test_palindrome_02(self):
        self.assertTrue( palindrome.palindrome("A") )
    def test_palindrome_03(self):
        self.assertTrue( palindrome.palindrome("Madam") )
    def test_palindrome_04(self):
        self.assertTrue( palindrome.palindrome("No lemon, no melon.") )
    def test_palindrome_05(self):
        self.assertTrue( palindrome.palindrome("A man, a plan, a canal: Panama.") )
    def test_palindrome_06(self):
        self.assertFalse( palindrome.palindrome("AB") )
    def test_palindrome_07(self):
        self.assertFalse( palindrome.palindrome("xyz") )
    def test_palindrome_03(self):
        self.assertFalse( palindrome.palindrome("Kanakana") )

if __name__ == "__main__":
    unittest.main()

