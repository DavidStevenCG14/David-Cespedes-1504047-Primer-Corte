#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: hola_test.py
# Description: Este programa prueba el modulo hola usando UnitTest
# Author: Diego Fernando Marin

# Standard Test imports
from __future__ import unicode_literals
import unittest
import sys

# Add the module location to the search path
sys.path.insert(0, '..') # the parent directory

# Module to be tested
import hola

class HolaTests(unittest.TestCase):
    def test_hola_noarg(self):
        self.assertEqual( 'Hola, Mundo!', hola.saludo() )
    def test_hola_none(self):
        self.assertEqual( 'Hola, Mundo!', hola.saludo(None) )
    def test_hola_empty(self):
        self.assertEqual( 'Hola, Mundo!', hola.saludo('') )
    def test_hola_01(self):
        self.assertEqual( 'Hola, Juana!', hola.saludo('Juana') )
    def test_hola_02(self):
        self.assertEqual( 'Hola, Diego!', hola.saludo('Diego') )

if __name__ == "__main__":
    unittest.main()

