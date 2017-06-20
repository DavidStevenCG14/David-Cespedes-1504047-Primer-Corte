#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: sums.py
# Description: This module outputs the sum of all multiples of C between A and B (included)
# Author: Diego Fernando Marin

def sum(first, last, number):
    """ (integer, integer, integer) -> integer
    return the sum of all integers between first and last, that are multiples of number
    """
    result = 0
    for value in range(first, last+1):
        if value % number == 0:
            result += value
    return result

def main():
    """ Main Program """
    first = int(input('first number:'))
    last = int(input('last number:'))
    number = int(input('which multiple:'))
    print(sum(first, last, number))

if __name__ == "__main__":
    main()

