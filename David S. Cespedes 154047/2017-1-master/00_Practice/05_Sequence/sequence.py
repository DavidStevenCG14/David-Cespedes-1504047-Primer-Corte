#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: sequence.py
# Description: This module outputs how many steps to reach a result of 1 for a given integer number
# Author: Diego Fernando Marin

def is_even(number):
    """ (integer) -> boolean
    return True if the number is even
    """
    return (number % 2) == 0

def is_odd(number):
    """ (integer) -> boolean
    return True if the number is odd
    """
    return not is_even(number)

def sequence(number):
    """ (integer) -> integer
    return how many steps until the result is 1, applying those rules:
      a. if the number is even, the next will be halt the number
      b. if the number is odd, the next will be triple the number plus one
    """
    result = 0
    while number != 1:
        if is_even(number):
            number = number // 2
        else: # is_odd(number)
            number = 3*number + 1
        result += 1
    return result

def main():
    """ Main Program """
    number = int(input('start number:'))
    print(sequence(number))

if __name__ == "__main__":
    main()

