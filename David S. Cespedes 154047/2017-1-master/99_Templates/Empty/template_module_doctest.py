#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: template_module_doctest.py
# Description: this module do yadda-yadda-yadda and doctested it
# Author: Diego Fernando Marin

def method(parameter):
    """ (parameter_type) -> result_type
    returns blah-blah-blah from blah-blah-blah 
    
    >>> method(argument1)
    result1
    >>> method(argument2)
    result2
    """
    pass

def main():
    """ Main Program """
    value = input("blah-blah-blah? : ")
    result = method(value)
    print("the result is ", result)

# Test
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

