#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: cubes.py
# Description: This module calculates the sum of the cubes of each integer from A to B (inclusive)
# Author: Diego Fernando Marin

import math

def cubes(numA, numB):
    """ (number, number) -> number
    return the sum of cubes of each integer from A to B (inclusive)
    """
    # TODO: return the correct value using loop
    total = 0 
    for number in range(numA, numB+1):
        total += number ** 3
    return total 
    
def main():
    """ Main Program """
    first = int(input("first number : "))
    last = int(input("last number : "))
    result = cubes(first, last)
    print("the sum of the cubes from {} to {} is {}".format(first, last, result))

if __name__ == "__main__":
    main()

