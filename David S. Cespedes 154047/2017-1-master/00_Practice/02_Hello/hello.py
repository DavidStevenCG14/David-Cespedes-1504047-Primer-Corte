#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: hello.py
# Description: This module outputs a salute according to its input
# Author: Diego Fernando Marin

def salute(name = 'World'):
    """ (string) -> string
    return a salute string based on its input,
    with no input, an empty string or None, the salute is "Hello, World!"
    with any other name like "Diego", the salute is "Hello, Diego!"
    """
    if name == None or name == '':
       name = 'World'
    return 'Hello, {}!'.format(name)

def main():
    """ Main Program """
    print(salute())

if __name__ == "__main__":
    main()

