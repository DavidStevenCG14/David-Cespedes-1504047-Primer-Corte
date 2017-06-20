#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: count.py
# Description: This module outputs how many multiples of C are between A and B (included)
# Author: Diego Fernando Marin

def count(first, last, number):
    """ (integer, integer, integer) -> integer
    return how many integers between first and last, are multiples of number
    """
    result = 0
    for value in range(first, last+1):
        if value % number == 0:
            result += 1
    return result

def main():
    """ Main Program """
    first = int(input('first number:'))
    last = int(input('last number:'))
    number = int(input('which multiple:'))
    print(count(first, last, number))

if __name__ == "__main__":
    main()

