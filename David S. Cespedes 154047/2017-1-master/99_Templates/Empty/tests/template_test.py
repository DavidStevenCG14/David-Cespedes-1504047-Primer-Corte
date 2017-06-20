#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: template_test.py
# Description: this program test if the module do yadda-yadda-yadda
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import template_module

class TemplateTests(unittest.TestCase):
    def test_method_arg1(self):
        self.assertEqual( 'result1', template_module.method(argument1) )
    def test_method_arg2(self):
        self.assertEqual( 'result2', template_module.method(argument2) )

if __name__ == '__main__':
    unittest.main()

