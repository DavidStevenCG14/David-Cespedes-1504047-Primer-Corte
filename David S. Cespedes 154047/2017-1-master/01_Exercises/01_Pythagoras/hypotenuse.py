#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: hypotenuse.py
# Description: This module calculates the hypotenuse given the two catheti (also known as legs)
# Author: Diego Fernando Marin

import math

def hypotenuse(cathetus1, cathetus2):
    """ (number, number) -> number
    return the hypotenuse from two catheti given as arguments
    """
    # TODO: return the correct value using the pythagorean theorem
    return math.sqrt(cathetus1**2 +  cathetus2**2)

def main():
    """ Main Program """
    c1 = float(input("cathetus 1: "))
    c2 = float(input("cathetus 2: "))
    result = hypotenuse(c1, c2)
    print("hypotenuse is", result)

if __name__ == "__main__":
    main()

