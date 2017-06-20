#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: palindrome.py
# Description: This module checks whenever a string is Palindrome or not
# Author: Diego Fernando Marin

def palindrome(sentence):
    """ (string) -> boolean
    return True if sentence is a palindrome, False otherwise
    """
    # TODO: return the correct value after checking the palindrome condition
    

    
    sentence = sentence.casefold()

    
    rev_sentence = reversed(sentence)

    
    if list(sentence) == list(rev_sentence):
       return True
    else:
       return False

def main():
    """ Main Program """
    sentence = input("sentence to check : ")
    result = palindrome(sentence)
    print("{} is a palindrome? {}".format(sentence, result))

if __name__ == "__main__":
    main()

